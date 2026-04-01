import { useState } from 'react'
import './App.css'
import Login from './components/login'
import UserView from './components/userView'
import HardwareSet from './components/hardwareSet'
import ProjectView from './components/projectView'

function App() {
  const [currentUser, setCurrentUser] = useState(null)
  const [showManager, setShowManager] = useState(false)
  const [selectedProject, setSelectedProject] = useState(null)

  function handleSignIn(user) {
    setCurrentUser(user)
  }

  function handleCreateAccount(user) {
    setCurrentUser(user)
  }

  if (showManager) {
    return <HardwareSet onBack={() => setShowManager(false)} user={currentUser} />
  }

  if (currentUser && selectedProject) {
    return (
      <ProjectView
        project={selectedProject}
        user={currentUser}
        onBack={() => setSelectedProject(null)}
      />
    )
  }

  if (currentUser) {
    return (
      <UserView
        user={currentUser}
        onLogout={() => { setCurrentUser(null); setSelectedProject(null) }}
        onSelectProject={p => setSelectedProject(p)}
      />
    )
  }

  return (
    <Login
      onSignIn={handleSignIn}
      onCreateAccount={handleCreateAccount}
      onManagerAccess={() => setShowManager(true)}
    />
  )
}

export default App
