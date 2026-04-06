// import { useState } from 'react'

// const MOCK_HW_SETS = [
//   { name: 'HWSet1', capacity: 100, available: 100 },
//   { name: 'HWSet2', capacity: 100, available: 100 },
// ]

// function StatusBanner({ status }) {
//   if (!status) return null
//   const isError = status.type === 'error'
//   return (
//     <div className={`pv-banner pv-banner--${isError ? 'error' : 'ok'}`}>
//       {status.message}
//     </div>
//   )
// }

// function HardwareCard({ hw, onCheckOut, onCheckIn }) {
//   const [checkOutQty, setCheckOutQty] = useState(1)
//   const [checkInQty, setCheckInQty] = useState(1)
//   const [status, setStatus] = useState(null)

//   const checkedOut = hw.capacity - hw.available
//   const availPct = hw.capacity > 0 ? Math.round((hw.available / hw.capacity) * 100) : 0
//   const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
//   const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

//   function handleCheckOut() {
//     if (checkOutQty > hw.available) {
//       setStatus({ type: 'error', message: `Only ${hw.available} units available.` })
//       return
//     }
//     if (checkOutQty < 1) return
//     onCheckOut(hw.name, checkOutQty)
//     setStatus({ type: 'ok', message: `Checked out ${checkOutQty} unit(s) of ${hw.name}.` })
//     setCheckOutQty(1)
//   }

//   function handleCheckIn() {
//     const currentlyOut = hw.capacity - hw.available
//     if (checkInQty > currentlyOut) {
//       setStatus({ type: 'error', message: `Only ${currentlyOut} units are checked out.` })
//       return
//     }
//     if (checkInQty < 1) return
//     onCheckIn(hw.name, checkInQty)
//     setStatus({ type: 'ok', message: `Checked in ${checkInQty} unit(s) of ${hw.name}.` })
//     setCheckInQty(1)
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
//             />
//             <button
//               className="hw-btn hw-btn--checkout"
//               onClick={handleCheckOut}
//               disabled={hw.available === 0}
//             >
//               Check Out
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
//             />
//             <button
//               className="hw-btn hw-btn--checkin"
//               onClick={handleCheckIn}
//               disabled={checkedOut === 0}
//             >
//               Check In
//             </button>
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }

// function ProjectView({ project, user, onBack }) {
//   const [hwSets, setHwSets] = useState(MOCK_HW_SETS)

//   function handleCheckOut(hwName, qty) {
//     setHwSets(prev =>
//       prev.map(hw =>
//         hw.name === hwName ? { ...hw, available: hw.available - qty } : hw
//       )
//     )
//   }

//   function handleCheckIn(hwName, qty) {
//     setHwSets(prev =>
//       prev.map(hw =>
//         hw.name === hwName
//           ? { ...hw, available: Math.min(hw.capacity, hw.available + qty) }
//           : hw
//       )
//     )
//   }

//   return (
//     <div className="hw-page">
//       <nav className="user-nav">
//         <div className="user-nav-title">
//           <span className="user-nav-app">Hardware-as-a-Service</span>
//           <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
//         </div>
//         <button className="logout-btn" onClick={onBack}>
//           <span className="logout-icon">&#x2190;</span> Back
//         </button>
//       </nav>

//       <main className="user-main">
//         <div className="pv-project-header">
//           <div className="pv-project-icon">&#128193;</div>
//           <div>
//             <h2 className="projects-heading" style={{ margin: 0 }}>{project.name}</h2>
//             {project.description && (
//               <p className="projects-subheading" style={{ margin: '4px 0 0' }}>{project.description}</p>
//             )}
//             <span className="pv-project-id">ID: {project.id}</span>
//           </div>
//         </div>

//         <div className="pv-info-banner">
//           &#x2139;&#xfe0f;&nbsp; Hardware resources are shared globally across all projects. Availability shown reflects current system-wide usage.
//         </div>

//         <h3 className="pv-section-heading">Hardware Resources</h3>

//         <div className="hw-grid">
//           {hwSets.map(hw => (
//             <HardwareCard
//               key={hw.name}
//               hw={hw}
//               onCheckOut={handleCheckOut}
//               onCheckIn={handleCheckIn}
//             />
//           ))}
//         </div>
//       </main>
//     </div>
//   )
// }

// export default ProjectView

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
    <div className={`pv-banner pv-banner--${isError ? 'error' : 'ok'}`}>
      {status.message}
    </div>
  )
}

function HardwareCard({ hw, projectId, userId, onAction }) {
  const [checkOutQty, setCheckOutQty] = useState(1)
  const [checkInQty, setCheckInQty] = useState(1)
  const [status, setStatus] = useState(null)
  const [loading, setLoading] = useState(null)

  const checkedOut = hw.capacity - hw.available
  const availPct =
    hw.capacity > 0 ? Math.round((hw.available / hw.capacity) * 100) : 0
  const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
  const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

  async function handleCheckOut() {
    if (!projectId) {
      setStatus({ type: 'error', message: 'Missing project ID.' })
      return
    }

    if (!userId) {
      setStatus({ type: 'error', message: 'No user ID — please log in.' })
      return
    }

    setLoading('out')
    setStatus(null)

    try {
      const data = await apiFetch('/check_out', {
        projectId,
        hwSetName: hw.name,
        qty: Number(checkOutQty),
        userId,
      })

      setStatus({
        type: data.success ? 'ok' : 'error',
        message: data.message || (data.success ? 'Checked out successfully.' : 'Check out failed.'),
      })

      if (data.success) {
        setCheckOutQty(1)
        await onAction()
      }
    } catch {
      setStatus({ type: 'error', message: 'Could not reach server.' })
    } finally {
      setLoading(null)
    }
  }

  async function handleCheckIn() {
    if (!projectId) {
      setStatus({ type: 'error', message: 'Missing project ID.' })
      return
    }

    if (!userId) {
      setStatus({ type: 'error', message: 'No user ID — please log in.' })
      return
    }

    setLoading('in')
    setStatus(null)

    try {
      const data = await apiFetch('/check_in', {
        projectId,
        hwSetName: hw.name,
        qty: Number(checkInQty),
        userId,
      })

      setStatus({
        type: data.success ? 'ok' : 'error',
        message: data.message || (data.success ? 'Checked in successfully.' : 'Check in failed.'),
      })

      if (data.success) {
        setCheckInQty(1)
        await onAction()
      }
    } catch {
      setStatus({ type: 'error', message: 'Could not reach server.' })
    } finally {
      setLoading(null)
    }
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
          <span className="hw-stat-val" style={{ color: availColor }}>
            {hw.available} units
          </span>
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
        <div
          className="hw-bar-fill"
          style={{ width: `${availPct}%`, background: barColor }}
        />
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
              max={Math.max(1, hw.available)}
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
              max={Math.max(1, checkedOut)}
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

function ProjectView({ project, user, onBack }) {
  const [projectDetails, setProjectDetails] = useState(project)
  const [hwSets, setHwSets] = useState([])
  const [pageStatus, setPageStatus] = useState(null)
  const [fetching, setFetching] = useState(true)

  const projectId = project?.projectId ?? project?.id

  const loadProjectAndHardware = useCallback(async () => {
    if (!projectId) {
      setPageStatus({ type: 'error', message: 'Missing project ID.' })
      setFetching(false)
      return
    }

    setFetching(true)

    try {
      const projectData = await apiFetch('/get_project_info', { projectId })

      if (projectData.success && projectData.project) {
        const p = projectData.project
        setProjectDetails({
          ...p,
          id: p.id ?? p.projectId ?? p._id,
          projectId: p.projectId ?? p.id ?? p._id,
          name: p.name ?? p.projectName ?? p.projectId,
          projectName: p.projectName ?? p.name ?? p.projectId,
          description: p.description ?? '',
        })
      }

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
          name: d.hardware.hwSetName ?? d.hardware.hwName ?? d.hardware.name,
          capacity: d.hardware.capacity ?? d.hardware.total ?? 0,
          available:
            d.hardware.available ??
            d.hardware.availability ??
            0,
        }))

      setHwSets(sets)
      setPageStatus(null)
    } catch {
      setPageStatus({ type: 'error', message: 'Could not reach server.' })
    } finally {
      setFetching(false)
    }
  }, [projectId])

  useEffect(() => {
    loadProjectAndHardware()
  }, [loadProjectAndHardware])

  return (
    <div className="hw-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">
            Logged in as: {user?.userId ?? 'unknown'}
          </span>
        </div>

        <button className="logout-btn" onClick={onBack}>
          <span className="logout-icon">&#x2190;</span> Back
        </button>
      </nav>

      <main className="user-main">
        <div className="pv-project-header">
          <div className="pv-project-icon">&#128193;</div>
          <div>
            <h2 className="projects-heading" style={{ margin: 0 }}>
              {projectDetails?.name ?? projectDetails?.projectName ?? 'Project'}
            </h2>

            {projectDetails?.description && (
              <p className="projects-subheading" style={{ margin: '4px 0 0' }}>
                {projectDetails.description}
              </p>
            )}

            <span className="pv-project-id">
              ID: {projectDetails?.projectId ?? projectDetails?.id ?? 'unknown'}
            </span>
          </div>
        </div>

        <div className="pv-info-banner">
          &#x2139;&#xfe0f;&nbsp; Hardware resources are shared globally across all projects.
          Availability shown reflects the current system-wide inventory.
        </div>

        <div style={{ marginBottom: 20 }}>
          <button
            className="hw-btn hw-btn--checkout"
            style={{ width: 'auto', padding: '10px 18px' }}
            onClick={loadProjectAndHardware}
            disabled={fetching}
          >
            {fetching ? 'Loading…' : '↻ Refresh'}
          </button>
        </div>

        <StatusBanner status={pageStatus} />

        <h3 className="pv-section-heading">Hardware Resources</h3>

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
                onAction={loadProjectAndHardware}
              />
            ))}
          </div>
        )}
      </main>
    </div>
  )
}

export default ProjectView