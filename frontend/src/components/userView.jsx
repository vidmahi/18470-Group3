function UserView({ user, projects = [], onLogout, onSelectProject, onCreateProject }) {
  return (
    <div className="user-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">Logged in as: {user?.email ?? 'unknown'}</span>
        </div>
        <button className="logout-btn" onClick={onLogout}>
          <span className="logout-icon">&#x2192;</span> Logout
        </button>
      </nav>

      <main className="user-main">
        <h2 className="projects-heading">My Projects</h2>
        <p className="projects-subheading">Select a project or create a new one to manage hardware resources</p>

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
                  <span className="project-desc">{project.description}</span>
                </div>
                <span className="project-chevron">&#62;</span>
              </div>
            </button>
          ))}

          <button className="project-card project-card--create" onClick={onCreateProject}>
            <div className="project-card-inner">
              <span className="project-icon">&#128194;</span>
              <div className="project-info">
                <span className="project-name">Create New Project</span>
                <span className="project-desc">Start a new hardware project</span>
              </div>
            </div>
          </button>
        </div>
      </main>
    </div>
  )
}

export default UserView
