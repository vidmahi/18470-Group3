// import { useState, useEffect, useCallback } from 'react'

// const API = 'http://localhost:5001'

// async function apiFetch(path, body) {
//   const res = await fetch(`${API}${path}`, {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     credentials: 'include',
//     body: JSON.stringify(body),
//   })
//   return res.json()
// }

// function StatusBanner({ status }) {
//   if (!status) return null
//   const isError = status.type === 'error'
//   return (
//     <div style={{
//       padding: '10px 16px',
//       borderRadius: 8,
//       marginBottom: 12,
//       fontSize: '0.9rem',
//       fontWeight: 500,
//       background: isError ? '#fef2f2' : '#f0fdf4',
//       color: isError ? '#b91c1c' : '#15803d',
//       border: `1px solid ${isError ? '#fecaca' : '#bbf7d0'}`,
//     }}>
//       {status.message}
//     </div>
//   )
// }

// function HardwareCard({ hw, projectId, userId, onAction }) {
//   const [checkOutQty, setCheckOutQty] = useState(1)
//   const [checkInQty, setCheckInQty] = useState(1)
//   const [status, setStatus] = useState(null)
//   const [loading, setLoading] = useState(null) // 'out' | 'in'

//   const checkedOut = hw.capacity - hw.available
//   const availPct = hw.capacity > 0 ? Math.round((hw.available / hw.capacity) * 100) : 0
//   const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
//   const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

//   async function handleCheckOut() {
//     if (!projectId) { setStatus({ type: 'error', message: 'Enter a Project ID above first.' }); return }
//     if (!userId) { setStatus({ type: 'error', message: 'No user ID — please log in.' }); return }
//     setLoading('out')
//     setStatus(null)
//     const data = await apiFetch('/check_out', {
//       projectId,
//       hwSetName: hw.name,
//       qty: checkOutQty,
//       userId,
//     })
//     setStatus({ type: data.success ? 'ok' : 'error', message: data.message })
//     if (data.success) onAction()
//     setLoading(null)
//   }

//   async function handleCheckIn() {
//     if (!projectId) { setStatus({ type: 'error', message: 'Enter a Project ID above first.' }); return }
//     if (!userId) { setStatus({ type: 'error', message: 'No user ID — please log in.' }); return }
//     setLoading('in')
//     setStatus(null)
//     const data = await apiFetch('/check_in', {
//       projectId,
//       hwSetName: hw.name,
//       qty: checkInQty,
//       userId,
//     })
//     setStatus({ type: data.success ? 'ok' : 'error', message: data.message })
//     if (data.success) onAction()
//     setLoading(null)
//   }

//   return (
//     <div className="hw-card">
//       <div className="hw-card-header">
//         <div className="hw-icon">&#128187;</div>
//         <div>
//           <div className="hw-name">{hw.name}</div>
//           <div className="hw-label">Hardware Set</div>
//         </div>
//       </div>

//       <div className="hw-stats">
//         <div className="hw-stat-row">
//           <span className="hw-stat-key">Capacity:</span>
//           <span className="hw-stat-val">{hw.capacity} units</span>
//         </div>
//         <div className="hw-stat-row">
//           <span className="hw-stat-key">Available:</span>
//           <span className="hw-stat-val" style={{ color: availColor }}>{hw.available} units</span>
//         </div>
//         <div className="hw-stat-row">
//           <span className="hw-stat-key">Checked Out:</span>
//           <span className="hw-stat-val">{checkedOut} units</span>
//         </div>
//       </div>

//       <div className="hw-bar-label">
//         <span>Availability</span>
//         <span>{availPct}%</span>
//       </div>
//       <div className="hw-bar-track">
//         <div className="hw-bar-fill" style={{ width: `${availPct}%`, background: barColor }} />
//       </div>

//       <StatusBanner status={status} />

//       <div className="hw-actions">
//         <div className="hw-action-row">
//           <label className="hw-action-label">Check Out</label>
//           <div className="hw-action-inputs">
//             <input
//               className="hw-qty-input"
//               type="number"
//               min="1"
//               max={hw.available}
//               value={checkOutQty}
//               onChange={e => setCheckOutQty(Math.max(1, Number(e.target.value)))}
//               disabled={loading === 'out'}
//             />
//             <button
//               className="hw-btn hw-btn--checkout"
//               onClick={handleCheckOut}
//               disabled={!!loading || hw.available === 0}
//             >
//               {loading === 'out' ? 'Working…' : 'Check Out'}
//             </button>
//           </div>
//         </div>

//         <div className="hw-action-row">
//           <label className="hw-action-label">Check In</label>
//           <div className="hw-action-inputs">
//             <input
//               className="hw-qty-input"
//               type="number"
//               min="1"
//               max={checkedOut}
//               value={checkInQty}
//               onChange={e => setCheckInQty(Math.max(1, Number(e.target.value)))}
//               disabled={loading === 'in'}
//             />
//             <button
//               className="hw-btn hw-btn--checkin"
//               onClick={handleCheckIn}
//               disabled={!!loading || checkedOut === 0}
//             >
//               {loading === 'in' ? 'Working…' : 'Check In'}
//             </button>
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }

// function HardwareSet({ onBack, user }) {
//   const [hwSets, setHwSets] = useState([])
//   const [projectId, setProjectId] = useState('')
//   const [pageStatus, setPageStatus] = useState(null)
//   const [fetching, setFetching] = useState(true)

//   const loadHardware = useCallback(async () => {
//     setFetching(true)
//     try {
//       const namesData = await apiFetch('/get_all_hw_names', {})
//       if (!namesData.success) {
//         setPageStatus({ type: 'error', message: 'Failed to load hardware sets.' })
//         setFetching(false)
//         return
//       }
//       const names = namesData.hardwareNames ?? []
//       const details = await Promise.all(
//         names.map(name => apiFetch('/get_hw_info', { hwSetName: name }))
//       )
//       const sets = details
//         .filter(d => d.success)
//         .map(d => ({
//           name: d.hardware.hwSetName ?? d.hardware.name,
//           capacity: d.hardware.capacity ?? d.hardware.total ?? 0,
//           available: d.hardware.available ?? 0,
//         }))
//       setHwSets(sets)
//       setPageStatus(null)
//     } catch {
//       setPageStatus({ type: 'error', message: 'Could not reach server.' })
//     }
//     setFetching(false)
//   }, [])

//   useEffect(() => { loadHardware() }, [loadHardware])

//   return (
//     <div className="hw-page">
//       <nav className="user-nav">
//         <div className="user-nav-title">
//           <span className="user-nav-app">Hardware-as-a-Service</span>
//           <span className="user-nav-email">
//             {user ? `Logged in as: ${user.userId}` : 'Manager View'}
//           </span>
//         </div>
//         <button className="logout-btn" onClick={onBack}>
//           <span className="logout-icon">&#x2190;</span> Back
//         </button>
//       </nav>

//       <main className="user-main">
//         <h2 className="projects-heading">Hardware Resources</h2>
//         <p className="projects-subheading">Check out or return hardware units for a project</p>

//         <div style={{ marginBottom: 24, display: 'flex', alignItems: 'center', gap: 12, flexWrap: 'wrap' }}>
//           <label style={{ fontWeight: 600, fontSize: '0.95rem', color: '#344054' }}>
//             Project ID:
//           </label>
//           <input
//             className="hw-qty-input"
//             style={{ width: 180 }}
//             type="text"
//             placeholder="e.g. proj-001"
//             value={projectId}
//             onChange={e => setProjectId(e.target.value)}
//           />
//           <button
//             className="hw-btn hw-btn--checkout"
//             style={{ width: 'auto', padding: '8px 16px' }}
//             onClick={loadHardware}
//             disabled={fetching}
//           >
//             {fetching ? 'Loading…' : '↻ Refresh'}
//           </button>
//         </div>

//         <StatusBanner status={pageStatus} />

//         {fetching && hwSets.length === 0 ? (
//           <p style={{ color: '#667085' }}>Loading hardware sets…</p>
//         ) : hwSets.length === 0 ? (
//           <p style={{ color: '#667085' }}>No hardware sets found.</p>
//         ) : (
//           <div className="hw-grid">
//             {hwSets.map(hw => (
//               <HardwareCard
//                 key={hw.name}
//                 hw={hw}
//                 projectId={projectId}
//                 userId={user?.userId ?? ''}
//                 onAction={loadHardware}
//               />
//             ))}
//           </div>
//         )}
//       </main>
//     </div>
//   )
// }

// export default HardwareSet

import { useState, useEffect, useCallback } from 'react'
import { apiUrl } from '../config'

async function apiFetch(path, body) {
  const res = await fetch(apiUrl(path), {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(body),
  })
  return res.json()
}

function StatusBanner({ status }) {
  if (!status) return null
  const isError = status.type === 'error'
  return (
    <div style={{
      padding: '10px 16px',
      borderRadius: 8,
      marginBottom: 12,
      fontSize: '0.9rem',
      fontWeight: 500,
      background: isError ? '#fef2f2' : '#f0fdf4',
      color: isError ? '#b91c1c' : '#15803d',
      border: `1px solid ${isError ? '#fecaca' : '#bbf7d0'}`,
    }}>
      {status.message}
    </div>
  )
}

function HardwareCard({ hw, projectId, userId, onAction }) {
  const [checkOutQty, setCheckOutQty] = useState(1)
  const [checkInQty, setCheckInQty] = useState(1)
  const [status, setStatus] = useState(null)
  const [loading, setLoading] = useState(null) // 'out' | 'in'

  const checkedOut = hw.capacity - hw.available
  const availPct = hw.capacity > 0 ? Math.round((hw.available / hw.capacity) * 100) : 0
  const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
  const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

  async function handleCheckOut() {
    if (!projectId) { setStatus({ type: 'error', message: 'Enter a Project ID above first.' }); return }
    if (!userId) { setStatus({ type: 'error', message: 'No user ID — please log in.' }); return }
    setLoading('out')
    setStatus(null)
    const data = await apiFetch('/check_out', {
      projectId,
      hwSetName: hw.name,
      qty: checkOutQty,
      userId,
    })
    setStatus({ type: data.success ? 'ok' : 'error', message: data.message })
    if (data.success) onAction()
    setLoading(null)
  }

  async function handleCheckIn() {
    if (!projectId) { setStatus({ type: 'error', message: 'Enter a Project ID above first.' }); return }
    if (!userId) { setStatus({ type: 'error', message: 'No user ID — please log in.' }); return }
    setLoading('in')
    setStatus(null)
    const data = await apiFetch('/check_in', {
      projectId,
      hwSetName: hw.name,
      qty: checkInQty,
      userId,
    })
    setStatus({ type: data.success ? 'ok' : 'error', message: data.message })
    if (data.success) onAction()
    setLoading(null)
  }

  return (
    <div className="hw-card">
      <div className="hw-card-header">
        <div className="hw-icon">&#128187;</div>
        <div>
          <div className="hw-name">{hw.name}</div>
          <div className="hw-label">Hardware Set</div>
        </div>
      </div>

      <div className="hw-stats">
        <div className="hw-stat-row">
          <span className="hw-stat-key">Capacity:</span>
          <span className="hw-stat-val">{hw.capacity} units</span>
        </div>
        <div className="hw-stat-row">
          <span className="hw-stat-key">Available:</span>
          <span className="hw-stat-val" style={{ color: availColor }}>{hw.available} units</span>
        </div>
        <div className="hw-stat-row">
          <span className="hw-stat-key">Checked Out:</span>
          <span className="hw-stat-val">{checkedOut} units</span>
        </div>
      </div>

      <div className="hw-bar-label">
        <span>Availability</span>
        <span>{availPct}%</span>
      </div>
      <div className="hw-bar-track">
        <div className="hw-bar-fill" style={{ width: `${availPct}%`, background: barColor }} />
      </div>

      <StatusBanner status={status} />

      <div className="hw-actions">
        <div className="hw-action-row">
          <label className="hw-action-label">Check Out</label>
          <div className="hw-action-inputs">
            <input
              className="hw-qty-input"
              type="number"
              min="1"
              max={hw.available}
              value={checkOutQty}
              onChange={e => setCheckOutQty(Math.max(1, Number(e.target.value)))}
              disabled={loading === 'out'}
            />
            <button
              className="hw-btn hw-btn--checkout"
              onClick={handleCheckOut}
              disabled={!!loading || hw.available === 0}
            >
              {loading === 'out' ? 'Working…' : 'Check Out'}
            </button>
          </div>
        </div>

        <div className="hw-action-row">
          <label className="hw-action-label">Check In</label>
          <div className="hw-action-inputs">
            <input
              className="hw-qty-input"
              type="number"
              min="1"
              max={checkedOut}
              value={checkInQty}
              onChange={e => setCheckInQty(Math.max(1, Number(e.target.value)))}
              disabled={loading === 'in'}
            />
            <button
              className="hw-btn hw-btn--checkin"
              onClick={handleCheckIn}
              disabled={!!loading || checkedOut === 0}
            >
              {loading === 'in' ? 'Working…' : 'Check In'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

function HardwareSet({ onBack, user }) {
  const [hwSets, setHwSets] = useState([])
  const [projectId, setProjectId] = useState('')
  const [pageStatus, setPageStatus] = useState(null)
  const [fetching, setFetching] = useState(true)

  const loadHardware = useCallback(async () => {
    setFetching(true)
    try {
      const namesData = await apiFetch('/get_all_hw_names', {})
      if (!namesData.success) {
        setPageStatus({ type: 'error', message: 'Failed to load hardware sets.' })
        setFetching(false)
        return
      }
      const names = namesData.hardwareNames ?? []
      const details = await Promise.all(
        names.map(name => apiFetch('/get_hw_info', { hwSetName: name }))
      )
      const sets = details
        .filter(d => d.success)
        .map(d => ({
          name: d.hardware.hwSetName ?? d.hardware.name,
          capacity: d.hardware.capacity ?? d.hardware.total ?? 0,
          available: d.hardware.available ?? d.hardware.availability ?? 0,
        }))
      setHwSets(sets)
      setPageStatus(null)
    } catch {
      setPageStatus({ type: 'error', message: 'Could not reach server.' })
    }
    setFetching(false)
  }, [])

  useEffect(() => { loadHardware() }, [loadHardware])

  return (
    <div className="hw-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">
            {user ? `Logged in as: ${user.userId}` : 'Manager View'}
          </span>
        </div>
        <button className="logout-btn" onClick={onBack}>
          <span className="logout-icon">&#x2190;</span> Back
        </button>
      </nav>

      <main className="user-main">
        <h2 className="projects-heading">Hardware Resources</h2>
        <p className="projects-subheading">Check out or return hardware units for a project</p>

        <div style={{ marginBottom: 24, display: 'flex', alignItems: 'center', gap: 12, flexWrap: 'wrap' }}>
          <label style={{ fontWeight: 600, fontSize: '0.95rem', color: '#344054' }}>
            Project ID:
          </label>
          <input
            className="hw-qty-input"
            style={{ width: 180 }}
            type="text"
            placeholder="e.g. proj-001"
            value={projectId}
            onChange={e => setProjectId(e.target.value)}
          />
          <button
            className="hw-btn hw-btn--checkout"
            style={{ width: 'auto', padding: '8px 16px' }}
            onClick={loadHardware}
            disabled={fetching}
          >
            {fetching ? 'Loading…' : '↻ Refresh'}
          </button>
        </div>

        <StatusBanner status={pageStatus} />

        {fetching && hwSets.length === 0 ? (
          <p style={{ color: '#667085' }}>Loading hardware sets…</p>
        ) : hwSets.length === 0 ? (
          <p style={{ color: '#667085' }}>No hardware sets found.</p>
        ) : (
          <div className="hw-grid">
            {hwSets.map(hw => (
              <HardwareCard
                key={hw.name}
                hw={hw}
                projectId={projectId}
                userId={user?.userId ?? ''}
                onAction={loadHardware}
              />
            ))}
          </div>
        )}
      </main>
    </div>
  )
}

export default HardwareSet