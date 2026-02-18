import './App.css'

function App() {
  return (
    <div className="app-page">
      <header className="app-header">
        <h1>Hardware-as-a-Service</h1>
        <p>Student Resource Management System</p>
      </header>

      <main className="login-card">
        <h2>Sign In</h2>

        <form className="login-form">
          <label htmlFor="user-id">User ID</label>
          <div className="input-wrapper">
            <span aria-hidden="true" className="input-icon">
              &#128100;
            </span>
            <input id="user-id" type="text" placeholder="Enter your user ID" />
          </div>

          <label htmlFor="password">Password</label>
          <div className="input-wrapper">
            <span aria-hidden="true" className="input-icon">
              &#128274;
            </span>
            <input id="password" type="password" placeholder="Enter your password" />
          </div>

          <button type="submit">Sign In</button>
        </form>

        <div className="card-divider" />
        <a href="#" className="create-account-link">
          New user? Create an account
        </a>
      </main>

      <footer className="demo-note">Demo: Enter any User ID to continue</footer>
    </div>
  )
}

export default App
