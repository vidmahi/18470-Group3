import { useState } from 'react'

function Login({ onSignIn, onCreateAccount }) {
  const [showCreate, setShowCreate] = useState(false)

  // Store user types
  const [userId, setUserId] = useState('')
  const [password, setPassword] = useState('')
  const [status, setStatus] = useState('')

  // Call Backend
  async function handleSignIN(e) {
    e.preventDefault()
    setStatus('Sending information...')

    try {
      const res = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, password })
      })
  
    const data = await res.json().catch(() => ({}))
    setStatus('Backend replied: ' + JSON.stringify(data))
    } catch (err) {
      setStatus('Failed to reach backend. Is Flask running?')
    }

  }

  return (
    <div className="app-page">
      <header className="app-header">
        <h1>Hardware-as-a-Service</h1>
        <p>Student Resource Management System</p>
      </header>

      {!showCreate ? (
        <main className="login-card">
          <h2>Sign In</h2>

          <form className="login-form" onSubmit={handleSignIN}>
            <label htmlFor="user-id">User ID</label>
            <div className="input-wrapper">
              <span aria-hidden="true" className="input-icon">&#128100;</span>
              <input id="user-id" type="text" placeholder="Enter your user ID" />
            </div>

            <label htmlFor="password">Password</label>
            <div className="input-wrapper">
              <span aria-hidden="true" className="input-icon">&#128274;</span>
              <input id="password" type="password" placeholder="Enter your password" />
            </div>
            <p className="encryption-note">Passwords are secured with bcrypt encryption algorithm</p>

            <button type="submit">Sign In</button>

            {status && <p style={{ marginTop: 12}}>{status}</p>}
          </form>

          <div className="card-divider" />
          <a href="#" className="create-account-link" onClick={e => { e.preventDefault(); setShowCreate(true) }}>
            New user? Create an account
          </a>
        </main>
      ) : (
        <main className="login-card">
          <h2>Create New Account</h2>

          <form className="login-form" onSubmit={onCreateAccount}>
            <label htmlFor="new-user-id">User ID</label>
            <div className="input-wrapper">
              <span aria-hidden="true" className="input-icon">&#128100;</span>
              <input id="new-user-id" type="text" placeholder="Enter your user ID" />
            </div>

            <label htmlFor="new-password">Password</label>
            <div className="input-wrapper">
              <span aria-hidden="true" className="input-icon">&#128274;</span>
              <input id="new-password" type="password" placeholder="Enter your password" />
            </div>
            <p className="encryption-note">Passwords are secured with bcrypt encryption algorithm</p>

            <button type="submit">Create Account</button>
          </form>

          <div className="card-divider" />
          <a href="#" className="create-account-link" onClick={e => { e.preventDefault(); setShowCreate(false) }}>
            Already have an account? Sign in
          </a>
        </main>
      )}

      <footer className="demo-note">Demo: Enter any User ID to continue</footer>
    </div>
  )
}

export default Login
