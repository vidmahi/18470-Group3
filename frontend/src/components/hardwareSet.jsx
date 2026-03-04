import { useState } from 'react'

const MOCK_SETS = [
  { id: 'hw1', name: 'HWSet1', capacity: 100, available: 45 },
  { id: 'hw2', name: 'HWSet2', capacity: 100, available: 23 },
]

function HardwareCard({ hw }) {
  const [checkOutQty, setCheckOutQty] = useState(1)
  const [checkInQty, setCheckInQty] = useState(1)
  const checkedOut = hw.capacity - hw.available
  const availPct = Math.round((hw.available / hw.capacity) * 100)
  const barColor = availPct >= 40 ? '#22c55e' : '#f97316'
  const availColor = availPct >= 40 ? '#16a34a' : '#dc2626'

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
              onChange={e => setCheckOutQty(Number(e.target.value))}
            />
            <button className="hw-btn hw-btn--checkout">Check Out</button>
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
              onChange={e => setCheckInQty(Number(e.target.value))}
            />
            <button className="hw-btn hw-btn--checkin">Check In</button>
          </div>
        </div>
      </div>
    </div>
  )
}

function HardwareSet({ onBack }) {
  return (
    <div className="hw-page">
      <nav className="user-nav">
        <div className="user-nav-title">
          <span className="user-nav-app">Hardware-as-a-Service</span>
          <span className="user-nav-email">Manager View</span>
        </div>
        <button className="logout-btn" onClick={onBack}>
          <span className="logout-icon">&#x2190;</span> Back
        </button>
      </nav>

      <main className="user-main">
        <h2 className="projects-heading">Hardware Resources</h2>
        <div className="hw-grid">
          {MOCK_SETS.map(hw => <HardwareCard key={hw.id} hw={hw} />)}
        </div>
      </main>
    </div>
  )
}

export default HardwareSet
