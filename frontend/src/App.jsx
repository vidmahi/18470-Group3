import { useState } from 'react'
import './App.css'
import Login from './components/login'
import UserView from './components/userView'
import HardwareSet from './components/hardwareSet'

function App() {
  const [currentUser, setCurrentUser] = useState(null)
  const [showManager, setShowManager] = useState(false)

  // TODO: hook — replace with sign-in API call
  function handleSignIn(e) {
    e.preventDefault()
    setCurrentUser({ email: 'user@utexas.edu' })
  }

  // TODO: hook — replace with create-account API call
  function handleCreateAccount(e) {
    e.preventDefault()
  }

  if (showManager) {
    return <HardwareSet onBack={() => setShowManager(false)} />
  }

  if (currentUser) {
    return (
      <UserView
        user={currentUser}
        projects={[]}
        onLogout={() => setCurrentUser(null)}
        onSelectProject={(p) => console.log('selected', p)}
        onCreateProject={() => console.log('create new')}
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
