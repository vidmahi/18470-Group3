// // // import { useState, useEffect } from 'react'
// // // import CreateProject from './createProject'

// // // function UserView({ user, onLogout, onSelectProject }) {
// // //   const [projects, setProjects] = useState([])
// // //   const [showCreate, setShowCreate] = useState(false)
// // //   const [loadingProjects, setLoadingProjects] = useState(true)

// // //   useEffect(() => {
// // //     async function fetchProjects() {
// // //       try {
// // //         const res = await fetch('http://localhost:5001/get_user_projects_list', {
// // //           method: 'POST',
// // //           headers: { 'Content-Type': 'application/json' },
// // //           credentials: 'include',
// // //           body: JSON.stringify({ userId: user.userId }),
// // //         })
// // //         const data = await res.json()
// // //         if (data.success) {
// // //           const list = (data.projects || []).map(p =>
// // //             typeof p === 'string' ? { id: p, name: p, description: '' } : p
// // //           )
// // //           setProjects(list)
// // //         }
// // //       } catch {
// // //         // silently fail — list stays empty
// // //       } finally {
// // //         setLoadingProjects(false)
// // //       }
// // //     }
// // //     fetchProjects()
// // //   }, [user.userId])

// // //   function handleProjectCreated(newProject) {
// // //     setProjects(prev => [...prev, newProject])
// // //     setShowCreate(false)
// // //   }

// // //   return (
// // //     <div className="user-page">
// // //       <nav className="user-nav">
// // //         <div className="user-nav-title">
// // //           <span className="user-nav-app">Hardware-as-a-Service</span>
// // //           <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
// // //         </div>
// // //         <button className="logout-btn" onClick={onLogout}>
// // //           <span className="logout-icon">&#x2192;</span> Logout
// // //         </button>
// // //       </nav>

// // //       <main className="user-main">
// // //         <div className="projects-header-row">
// // //           <div>
// // //             <h2 className="projects-heading">My Projects</h2>
// // //             <p className="projects-subheading">Select a project or create a new one to manage hardware resources</p>
// // //           </div>
// // //           <button className="new-project-btn" onClick={() => setShowCreate(true)}>
// // //             + New Project
// // //           </button>
// // //         </div>

// // //         {loadingProjects ? (
// // //           <p className="projects-loading">Loading projects…</p>
// // //         ) : (
// // //           <div className="projects-grid">
// // //             {projects.map(project => (
// // //               <button
// // //                 key={project.id}
// // //                 className="project-card"
// // //                 onClick={() => onSelectProject?.(project)}
// // //               >
// // //                 <div className="project-card-inner">
// // //                   <span className="project-icon">&#128193;</span>
// // //                   <div className="project-info">
// // //                     <span className="project-name">{project.name}</span>
// // //                     <span className="project-desc">{project.description || project.id}</span>
// // //                   </div>
// // //                   <span className="project-chevron">&#62;</span>
// // //                 </div>
// // //               </button>
// // //             ))}

// // //             {projects.length === 0 && (
// // //               <div className="projects-empty">
// // //                 <span style={{ fontSize: '2rem' }}>&#128193;</span>
// // //                 <p>No projects yet. Create your first one!</p>
// // //               </div>
// // //             )}
// // //           </div>
// // //         )}
// // //       </main>

// // //       {showCreate && (
// // //         <CreateProject
// // //           userId={user.userId}
// // //           onSuccess={handleProjectCreated}
// // //           onClose={() => setShowCreate(false)}
// // //         />
// // //       )}
// // //     </div>
// // //   )
// // // }

// // // export default UserView

// // import { useState, useEffect } from 'react'
// // import CreateProject from './createProject'
// // import { apiUrl } from '../config'

// // function UserView({ user, onLogout, onSelectProject }) {
// //   const [projects, setProjects] = useState([])
// //   const [showCreate, setShowCreate] = useState(false)
// //   const [loadingProjects, setLoadingProjects] = useState(true)

// //   useEffect(() => {
// //     async function fetchProjects() {
// //       try {
// //         const res = await fetch(apiUrl('/get_user_projects_list'), {
// //           method: 'POST',
// //           headers: { 'Content-Type': 'application/json' },
// //           credentials: 'include',
// //           body: JSON.stringify({ userId: user.userId }),
// //         })
// //         const data = await res.json()
// //         if (data.success) {
// //           const list = (data.projects || []).map(p =>
// //             typeof p === 'string'
// //               ? { id: p, name: p, description: '' }
// //               : {
// //                   id: p.id ?? p.projectId ?? p._id,
// //                   name: p.name ?? p.projectName ?? p.projectId,
// //                   description: p.description ?? '',
// //                   ...p,
// //                 }
// //           )
// //           setProjects(list)
// //         }
// //       } catch {
// //         // silently fail — list stays empty
// //       } finally {
// //         setLoadingProjects(false)
// //       }
// //     }
// //     fetchProjects()
// //   }, [user.userId])

// //   function handleProjectCreated(newProject) {
// //     setProjects(prev => [...prev, newProject])
// //     setShowCreate(false)
// //   }

// //   return (
// //     <div className="user-page">
// //       <nav className="user-nav">
// //         <div className="user-nav-title">
// //           <span className="user-nav-app">Hardware-as-a-Service</span>
// //           <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
// //         </div>
// //         <button className="logout-btn" onClick={onLogout}>
// //           <span className="logout-icon">&#x2192;</span> Logout
// //         </button>
// //       </nav>

// //       <main className="user-main">
// //         <div className="projects-header-row">
// //           <div>
// //             <h2 className="projects-heading">My Projects</h2>
// //             <p className="projects-subheading">Select a project or create a new one to manage hardware resources</p>
// //           </div>
// //           <button className="new-project-btn" onClick={() => setShowCreate(true)}>
// //             + New Project
// //           </button>
// //         </div>

// //         {loadingProjects ? (
// //           <p className="projects-loading">Loading projects…</p>
// //         ) : (
// //           <div className="projects-grid">
// //             {projects.map(project => (
// //               <button
// //                 key={project.id ?? project.projectId ?? project._id}
// //                 className="project-card"
// //                 onClick={() => onSelectProject?.(project)}
// //               >
// //                 <div className="project-card-inner">
// //                   <span className="project-icon">&#128193;</span>
// //                   <div className="project-info">
// //                     <span className="project-name">{project.name ?? project.projectName}</span>
// //                     <span className="project-desc">{project.description || project.id || project.projectId}</span>
// //                   </div>
// //                   <span className="project-chevron">&#62;</span>
// //                 </div>
// //               </button>
// //             ))}

// //             {projects.length === 0 && (
// //               <div className="projects-empty">
// //                 <span style={{ fontSize: '2rem' }}>&#128193;</span>
// //                 <p>No projects yet. Create your first one!</p>
// //               </div>
// //             )}
// //           </div>
// //         )}
// //       </main>

// //       {showCreate && (
// //         <CreateProject
// //           userId={user.userId}
// //           onSuccess={handleProjectCreated}
// //           onClose={() => setShowCreate(false)}
// //         />
// //       )}
// //     </div>
// //   )
// // }

// // export default UserView

// import { useState, useEffect } from 'react'
// import CreateProject from './createProject'
// import { apiUrl } from '../config'

// function UserView({ user, onLogout, onSelectProject }) {
//   const [projects, setProjects] = useState([])
//   const [showCreate, setShowCreate] = useState(false)
//   const [loadingProjects, setLoadingProjects] = useState(true)
//   const [joinProjectId, setJoinProjectId] = useState('')
//   const [joinLoading, setJoinLoading] = useState(false)
//   const [joinError, setJoinError] = useState('')
//   const [joinSuccess, setJoinSuccess] = useState('')

//   async function fetchProjects() {
//     try {
//       setLoadingProjects(true)
//       const res = await fetch(apiUrl('/get_user_projects_list'), {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         credentials: 'include',
//         body: JSON.stringify({ userId: user.userId }),
//       })
//       const data = await res.json()
//       if (data.success) {
//         const list = (data.projects || []).map(p =>
//           typeof p === 'string'
//             ? { id: p, name: p, description: '' }
//             : {
//                 id: p.id ?? p.projectId ?? p._id,
//                 name: p.name ?? p.projectName ?? p.projectId,
//                 description: p.description ?? '',
//                 ...p,
//               }
//         )
//         setProjects(list)
//       }
//     } catch {
//       // silently fail
//     } finally {
//       setLoadingProjects(false)
//     }
//   }

//   useEffect(() => {
//     fetchProjects()
//   }, [user.userId])

//   function handleProjectCreated(newProject) {
//     setProjects(prev => [...prev, newProject])
//     setShowCreate(false)
//   }

//   async function handleJoinProject(e) {
//     e.preventDefault()
//     setJoinError('')
//     setJoinSuccess('')
//     setJoinLoading(true)

//     try {
//       const res = await fetch(apiUrl('/join_project'), {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         credentials: 'include',
//         body: JSON.stringify({
//           userId: user.userId,
//           projectId: joinProjectId,
//         }),
//       })

//       const data = await res.json()

//       if (data.success) {
//         setJoinSuccess('Joined project successfully')
//         setJoinProjectId('')
//         await fetchProjects()
//       } else {
//         setJoinError(data.message || 'Failed to join project')
//       }
//     } catch {
//       setJoinError('Could not reach server')
//     } finally {
//       setJoinLoading(false)
//     }
//   }

//   return (
//     <div className="user-page">
//       <nav className="user-nav">
//         <div className="user-nav-title">
//           <span className="user-nav-app">Hardware-as-a-Service</span>
//           <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
//         </div>
//         <button className="logout-btn" onClick={onLogout}>
//           <span className="logout-icon">&#x2192;</span> Logout
//         </button>
//       </nav>

//       <main className="user-main">
//         <div className="projects-header-row">
//           <div>
//             <h2 className="projects-heading">My Projects</h2>
//             <p className="projects-subheading">Select a project or create a new one to manage hardware resources</p>
//           </div>
//           <button className="new-project-btn" onClick={() => setShowCreate(true)}>
//             + New Project
//           </button>
//         </div>

//         <form onSubmit={handleJoinProject} style={{ marginBottom: 24, display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center' }}>
//           <input
//             className="hw-qty-input"
//             style={{ width: 220 }}
//             type="text"
//             placeholder="Enter project ID to join"
//             value={joinProjectId}
//             onChange={e => setJoinProjectId(e.target.value)}
//             required
//           />
//           <button className="new-project-btn" type="submit" disabled={joinLoading}>
//             {joinLoading ? 'Joining…' : 'Join Project'}
//           </button>
//           {joinError && <span style={{ color: '#d92d20', fontSize: '0.9rem' }}>{joinError}</span>}
//           {joinSuccess && <span style={{ color: '#15803d', fontSize: '0.9rem' }}>{joinSuccess}</span>}
//         </form>

//         {loadingProjects ? (
//           <p className="projects-loading">Loading projects…</p>
//         ) : (
//           <div className="projects-grid">
//             {projects.map(project => (
//               <button
//                 key={project.id ?? project.projectId ?? project._id}
//                 className="project-card"
//                 onClick={() => onSelectProject?.(project)}
//               >
//                 <div className="project-card-inner">
//                   <span className="project-icon">&#128193;</span>
//                   <div className="project-info">
//                     <span className="project-name">{project.name ?? project.projectName}</span>
//                     <span className="project-desc">{project.description || project.id || project.projectId}</span>
//                   </div>
//                   <span className="project-chevron">&#62;</span>
//                 </div>
//               </button>
//             ))}

//             {projects.length === 0 && (
//               <div className="projects-empty">
//                 <span style={{ fontSize: '2rem' }}>&#128193;</span>
//                 <p>No projects yet. Create your first one!</p>
//               </div>
//             )}
//           </div>
//         )}
//       </main>

//       {showCreate && (
//         <CreateProject
//           userId={user.userId}
//           onSuccess={handleProjectCreated}
//           onClose={() => setShowCreate(false)}
//         />
//       )}
//     </div>
//   )
// }

// export default UserView

import { useState, useEffect } from 'react'
import CreateProject from './createProject'
import { apiUrl } from '../config'

function UserView({ user, onLogout, onSelectProject }) {
  const [projects, setProjects] = useState([])
  const [showCreate, setShowCreate] = useState(false)
  const [loadingProjects, setLoadingProjects] = useState(true)

  const [joinProjectId, setJoinProjectId] = useState('')
  const [joinLoading, setJoinLoading] = useState(false)
  const [joinError, setJoinError] = useState('')
  const [joinSuccess, setJoinSuccess] = useState('')

  async function fetchProjects() {
    try {
      setLoadingProjects(true)

      const res = await fetch(apiUrl('/get_user_projects_list'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ userId: user.userId }),
      })

      const data = await res.json()

      if (data.success) {
        const list = (data.projects || []).map(p =>
          typeof p === 'string'
            ? {
                id: p,
                projectId: p,
                name: p,
                projectName: p,
                description: '',
              }
            : {
                ...p,
                id: p.id ?? p.projectId ?? p._id,
                projectId: p.projectId ?? p.id ?? p._id,
                name: p.name ?? p.projectName ?? p.projectId,
                projectName: p.projectName ?? p.name ?? p.projectId,
                description: p.description ?? '',
              }
        )

        setProjects(list)
      } else {
        setProjects([])
      }
    } catch {
      setProjects([])
    } finally {
      setLoadingProjects(false)
    }
  }

  useEffect(() => {
    fetchProjects()
  }, [user.userId])

  async function handleProjectCreated(newProject) {
    setShowCreate(false)
    setJoinError('')
    setJoinSuccess('Project created successfully')
    await fetchProjects()
  }

  async function handleJoinProject(e) {
    e.preventDefault()
    setJoinError('')
    setJoinSuccess('')
    setJoinLoading(true)

    try {
      const res = await fetch(apiUrl('/join_project'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
          userId: user.userId,
          projectId: joinProjectId.trim(),
        }),
      })

      const data = await res.json()

      if (data.success) {
        setJoinSuccess('Joined project successfully')
        setJoinProjectId('')
        await fetchProjects()
      } else {
        setJoinError(data.message || 'Failed to join project')
      }
    } catch {
      setJoinError('Could not reach server')
    } finally {
      setJoinLoading(false)
    }
  }

  return (
    <div className="user-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">
            Logged in as: {user?.userId ?? 'unknown'}
          </span>
        </div>

        <button className="logout-btn" onClick={onLogout}>
          <span className="logout-icon">&#x2192;</span> Logout
        </button>
      </nav>

      <main className="user-main">
        <div className="projects-header-row">
          <div>
            <h2 className="projects-heading">My Projects</h2>
            <p className="projects-subheading">
              Select a project or create a new one to manage hardware resources
            </p>
          </div>

          <button className="new-project-btn" onClick={() => setShowCreate(true)}>
            + New Project
          </button>
        </div>

        <form
          onSubmit={handleJoinProject}
          style={{
            marginBottom: 24,
            display: 'flex',
            gap: 12,
            flexWrap: 'wrap',
            alignItems: 'center',
          }}
        >
          <input
            className="hw-qty-input"
            style={{ width: 220 }}
            type="text"
            placeholder="Enter project ID to join"
            value={joinProjectId}
            onChange={e => setJoinProjectId(e.target.value)}
            required
          />

          <button className="new-project-btn" type="submit" disabled={joinLoading}>
            {joinLoading ? 'Joining…' : 'Join Project'}
          </button>

          {joinError && (
            <span style={{ color: '#d92d20', fontSize: '0.9rem' }}>
              {joinError}
            </span>
          )}

          {joinSuccess && (
            <span style={{ color: '#15803d', fontSize: '0.9rem' }}>
              {joinSuccess}
            </span>
          )}
        </form>

        {loadingProjects ? (
          <p className="projects-loading">Loading projects…</p>
        ) : (
          <div className="projects-grid">
            {projects.map(project => (
              <button
                key={project.id ?? project.projectId ?? project._id}
                className="project-card"
                onClick={() => onSelectProject?.(project)}
              >
                <div className="project-card-inner">
                  <span className="project-icon">&#128193;</span>

                  <div className="project-info">
                    <span className="project-name">
                      {project.name ?? project.projectName}
                    </span>
                    <span className="project-desc">
                      {project.description || project.projectId || project.id}
                    </span>
                  </div>

                  <span className="project-chevron">&#62;</span>
                </div>
              </button>
            ))}

            {projects.length === 0 && (
              <div className="projects-empty">
                <span style={{ fontSize: '2rem' }}>&#128193;</span>
                <p>No projects yet. Create your first one or join one by ID.</p>
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