import './App.css'
import Login from './components/login'

function App() {

  // TODO: hook — replace with sign-in API call
  function handleSignIn(e) {
    e.preventDefault()
  }

  // TODO: hook — replace with create-account API call
  function handleCreateAccount(e) {
    e.preventDefault()
  }

  return (
    <Login onSignIn={handleSignIn} onCreateAccount={handleCreateAccount} />
  )
}

export default App
