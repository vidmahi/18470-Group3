import { useState } from 'react'

const MOCK_HW_SETS = [
  { name: 'HWSet1', capacity: 100, available: 100 },
  { name: 'HWSet2', capacity: 100, available: 100 },
]

function StatusBanner({ status }) {
  if (!status) return null
  const isError = status.type === 'error'
  return (
    <div className={`pv-banner pv-banner--${isError ? 'error' : 'ok'}`}>
      {status.message}
    </div>
  )
}

function HardwareCard({ hw, onCheckOut, onCheckIn }) {
  const [checkOutQty, setCheckOutQty] = useState(1)
  const [checkInQty, setCheckInQty] = useState(1)
  const [status, setStatus] = useState(null)

  const checkedOut = hw.capacity - hw.available
  const availPct = hw.capacity > 0 ? Math.round((hw.available / hw.capacity) * 100) : 0
  const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
  const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

  function handleCheckOut() {
    if (checkOutQty > hw.available) {
      setStatus({ type: 'error', message: `Only ${hw.available} units available.` })
      return
    }
    if (checkOutQty < 1) return
    onCheckOut(hw.name, checkOutQty)
    setStatus({ type: 'ok', message: `Checked out ${checkOutQty} unit(s) of ${hw.name}.` })
    setCheckOutQty(1)
  }

  function handleCheckIn() {
    const currentlyOut = hw.capacity - hw.available
    if (checkInQty > currentlyOut) {
      setStatus({ type: 'error', message: `Only ${currentlyOut} units are checked out.` })
      return
    }
    if (checkInQty < 1) return
    onCheckIn(hw.name, checkInQty)
    setStatus({ type: 'ok', message: `Checked in ${checkInQty} unit(s) of ${hw.name}.` })
    setCheckInQty(1)
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
            />
            <button
              className="hw-btn hw-btn--checkout"
              onClick={handleCheckOut}
              disabled={hw.available === 0}
            >
              Check Out
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
            />
            <button
              className="hw-btn hw-btn--checkin"
              onClick={handleCheckIn}
              disabled={checkedOut === 0}
            >
              Check In
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

function ProjectView({ project, user, onBack }) {
  const [hwSets, setHwSets] = useState(MOCK_HW_SETS)

  function handleCheckOut(hwName, qty) {
    setHwSets(prev =>
      prev.map(hw =>
        hw.name === hwName ? { ...hw, available: hw.available - qty } : hw
      )
    )
  }

  function handleCheckIn(hwName, qty) {
    setHwSets(prev =>
      prev.map(hw =>
        hw.name === hwName
          ? { ...hw, available: Math.min(hw.capacity, hw.available + qty) }
          : hw
      )
    )
  }

  return (
    <div className="hw-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">Logged in as: {user?.userId ?? 'unknown'}</span>
        </div>
        <button className="logout-btn" onClick={onBack}>
          <span className="logout-icon">&#x2190;</span> Back
        </button>
      </nav>

      <main className="user-main">
        <div className="pv-project-header">
          <div className="pv-project-icon">&#128193;</div>
          <div>
            <h2 className="projects-heading" style={{ margin: 0 }}>{project.name}</h2>
            {project.description && (
              <p className="projects-subheading" style={{ margin: '4px 0 0' }}>{project.description}</p>
            )}
            <span className="pv-project-id">ID: {project.id}</span>
          </div>
        </div>

        <div className="pv-info-banner">
          &#x2139;&#xfe0f;&nbsp; Hardware resources are shared globally across all projects. Availability shown reflects current system-wide usage.
        </div>

        <h3 className="pv-section-heading">Hardware Resources</h3>

        <div className="hw-grid">
          {hwSets.map(hw => (
            <HardwareCard
              key={hw.name}
              hw={hw}
              onCheckOut={handleCheckOut}
              onCheckIn={handleCheckIn}
            />
          ))}
        </div>
      </main>
    </div>
  )
}

export default ProjectView
