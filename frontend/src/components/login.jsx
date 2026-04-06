// import { useState } from 'react'

// function Login({ onSignIn, onCreateAccount, onManagerAccess }) {
//   const [mode, setMode] = useState('login') // 'login' | 'signup'
//   const [userId, setUserId] = useState('')
//   const [password, setPassword] = useState('')
//   const [error, setError] = useState('')
//   const [loading, setLoading] = useState(false)

//   async function handleSubmit(e) {
//     e.preventDefault()
//     setError('')
//     setLoading(true)

//     const endpoint = mode === 'login' ? '/login' : '/add_user'
//     try {
//       const res = await fetch(`http://localhost:5001${endpoint}`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         credentials: 'include',
//         body: JSON.stringify({ userId, password }),
//       })
//       const data = await res.json()
//       if (data.success) {
//         if (mode === 'login') {
//           onSignIn({ userId })
//         } else {
//           onCreateAccount({ userId })
//         }
//       } else {
//         setError(data.message || 'Something went wrong')
//       }
//     } catch {
//       setError('Could not reach server')
//     } finally {
//       setLoading(false)
//     }
//   }

//   return (
//     <div className="app-page">
//       <div className="app-header">
//         <h1>Hardware-as-a-Service</h1>
//         <p>Manage hardware resources for your projects</p>
//       </div>

//       <div className="login-card">
//         <h2>{mode === 'login' ? 'Sign In' : 'Create Account'}</h2>

//         <form className="login-form" onSubmit={handleSubmit}>
//           <label>
//             User ID
//             <div className="input-wrapper">
//               <span className="input-icon">&#128100;</span>
//               <input
//                 type="text"
//                 placeholder="Enter your user ID"
//                 value={userId}
//                 onChange={e => setUserId(e.target.value)}
//                 required
//                 autoComplete="username"
//               />
//             </div>
//           </label>

//           <label>
//             Password
//             <div className="input-wrapper">
//               <span className="input-icon">&#128274;</span>
//               <input
//                 type="password"
//                 placeholder="Enter your password"
//                 value={password}
//                 onChange={e => setPassword(e.target.value)}
//                 required
//                 autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
//               />
//             </div>
//             {mode === 'signup' && (
//               <p className="encryption-note">Passwords are encrypted before storage.</p>
//             )}
//           </label>

//           {error && <p style={{ color: '#d92d20', fontSize: '0.9rem', margin: 0 }}>{error}</p>}

//           <button type="submit" disabled={loading}>
//             {loading ? 'Please wait…' : mode === 'login' ? 'Sign In' : 'Create Account'}
//           </button>
//         </form>

//         <div className="card-divider" />

//         {mode === 'login' ? (
//           <p style={{ margin: 0, fontSize: '0.95rem' }}>
//             No account?{' '}
//             <a className="create-account-link" href="#" onClick={e => { e.preventDefault(); setMode('signup'); setError('') }}>
//               Create one
//             </a>
//           </p>
//         ) : (
//           <p style={{ margin: 0, fontSize: '0.95rem' }}>
//             Already have an account?{' '}
//             <a className="create-account-link" href="#" onClick={e => { e.preventDefault(); setMode('login'); setError('') }}>
//               Sign in
//             </a>
//           </p>
//         )}
//       </div>

//       <p className="demo-note">ECE 461L &mdash; Spring 2025</p>

//       <button className="manager-btn" onClick={onManagerAccess}>
//         Manager Access
//       </button>
//     </div>
//   )
// }

// export default Login

import { useState } from 'react'
import { apiUrl } from '../config'

function Login({ onSignIn, onCreateAccount, onManagerAccess }) {
  const [mode, setMode] = useState('login') // 'login' | 'signup'
  const [userId, setUserId] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)

    const endpoint = mode === 'login' ? '/login' : '/add_user'
    try {
      const res = await fetch(apiUrl(endpoint), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ userId, password }),
      })
      const data = await res.json()
      if (data.success) {
        if (mode === 'login') {
          onSignIn({ userId })
        } else {
          onCreateAccount({ userId })
        }
      } else {
        setError(data.message || 'Something went wrong')
      }
    } catch {
      setError('Could not reach server')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-page">
      <div className="app-header">
        <h1>Hardware-as-a-Service</h1>
        <p>Manage hardware resources for your projects</p>
      </div>

      <div className="login-card">
        <h2>{mode === 'login' ? 'Sign In' : 'Create Account'}</h2>

        <form className="login-form" onSubmit={handleSubmit}>
          <label>
            User ID
            <div className="input-wrapper">
              <span className="input-icon">&#128100;</span>
              <input
                type="text"
                placeholder="Enter your user ID"
                value={userId}
                onChange={e => setUserId(e.target.value)}
                required
                autoComplete="username"
              />
            </div>
          </label>

          <label>
            Password
            <div className="input-wrapper">
              <span className="input-icon">&#128274;</span>
              <input
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                required
                autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
              />
            </div>
            {mode === 'signup' && (
              <p className="encryption-note">Passwords are encrypted before storage.</p>
            )}
          </label>

          {error && <p style={{ color: '#d92d20', fontSize: '0.9rem', margin: 0 }}>{error}</p>}

          <button type="submit" disabled={loading}>
            {loading ? 'Please wait…' : mode === 'login' ? 'Sign In' : 'Create Account'}
          </button>
        </form>

        <div className="card-divider" />

        {mode === 'login' ? (
          <p style={{ margin: 0, fontSize: '0.95rem' }}>
            No account?{' '}
            <a className="create-account-link" href="#" onClick={e => { e.preventDefault(); setMode('signup'); setError('') }}>
              Create one
            </a>
          </p>
        ) : (
          <p style={{ margin: 0, fontSize: '0.95rem' }}>
            Already have an account?{' '}
            <a className="create-account-link" href="#" onClick={e => { e.preventDefault(); setMode('login'); setError('') }}>
              Sign in
            </a>
          </p>
        )}
      </div>

      <p className="demo-note">ECE 461L &mdash; Spring 2025</p>

      <button className="manager-btn" onClick={onManagerAccess}>
        Manager Access
      </button>
    </div>
  )
}

export default Login