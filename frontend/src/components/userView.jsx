import { useState, useEffect } from 'react'
import CreateProject from './createProject'

function UserView({ user, onLogout, onSelectProject }) {
  const [projects, setProjects] = useState([])
  const [showCreate, setShowCreate] = useState(false)
  const [loadingProjects, setLoadingProjects] = useState(true)

  useEffect(() => {
    async function fetchProjects() {
      try {
        const res = await fetch('http://localhost:5001/get_user_projects_list', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ userId: user.userId }),
        })
        const data = await res.json()
        if (data.success) {
          const list = (data.projects || []).map(p =>
            typeof p === 'string' ? { id: p, name: p, description: '' } : p
          )
          setProjects(list)
        }
      } catch {
        // silently fail — list stays empty
      } finally {
        setLoadingProjects(false)
      }
    }
    fetchProjects()
  }, [user.userId])

  function handleProjectCreated(newProject) {
    setProjects(prev => [...prev, newProject])
    setShowCreate(false)
  }

  return (
    <div className="user-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
        </div>
        <button className="logout-btn" onClick={onLogout}>
          <span className="logout-icon">&#x2192;</span> Logout
        </button>
      </nav>

      <main className="user-main">
        <div className="projects-header-row">
          <div>
            <h2 className="projects-heading">My Projects</h2>
            <p className="projects-subheading">Select a project or create a new one to manage hardware resources</p>
          </div>
          <button className="new-project-btn" onClick={() => setShowCreate(true)}>
            + New Project
          </button>
        </div>

        {loadingProjects ? (
          <p className="projects-loading">Loading projects…</p>
        ) : (
          <div className="projects-grid">
            {projects.map(project => (
              <button
                key={project.id}
                className="project-card"
                onClick={() => onSelectProject?.(project)}
              >
                <div className="project-card-inner">
                  <span className="project-icon">&#128193;</span>
                  <div className="project-info">
                    <span className="project-name">{project.name}</span>
                    <span className="project-desc">{project.description || project.id}</span>
                  </div>
                  <span className="project-chevron">&#62;</span>
                </div>
              </button>
            ))}

            {projects.length === 0 && (
              <div className="projects-empty">
                <span style={{ fontSize: '2rem' }}>&#128193;</span>
                <p>No projects yet. Create your first one!</p>
              </div>
            )}
          </div>
        )}
      </main>

      {showCreate && (
        <CreateProject
          userId={user.userId}
          onSuccess={handleProjectCreated}
          onClose={() => setShowCreate(false)}
        />
      )}
    </div>
  )
}

export default UserView
