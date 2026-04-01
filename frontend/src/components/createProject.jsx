import { useState } from 'react'

function CreateProject({ userId, onSuccess, onClose }) {
  const [projectName, setProjectName] = useState('')
  const [projectId, setProjectId] = useState('')
  const [description, setDescription] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const res = await fetch('http://localhost:5001/create_project', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ projectName, projectId, description }),
      })
      const data = await res.json()
      if (data.success) {
        onSuccess({ id: projectId, name: projectName, description })
      } else {
        setError(data.message || 'Failed to create project')
      }
    } catch {
      setError('Could not reach server')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-card" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h2>New Project</h2>
          <button className="modal-close" onClick={onClose}>&#x2715;</button>
        </div>
        <p className="modal-subheading">Fill in the details to start a new hardware project</p>

        <form className="modal-form" onSubmit={handleSubmit}>
          <label>
            Project Name
            <input
              type="text"
              placeholder="e.g. Autonomous Rover"
              value={projectName}
              onChange={e => setProjectName(e.target.value)}
              required
            />
          </label>

          <label>
            Project ID
            <input
              type="text"
              placeholder="e.g. proj-001 (must be unique)"
              value={projectId}
              onChange={e => setProjectId(e.target.value)}
              required
            />
          </label>

          <label>
            Description
            <textarea
              placeholder="Brief description of your project..."
              value={description}
              onChange={e => setDescription(e.target.value)}
              rows={3}
              required
            />
          </label>

          {error && <p className="modal-error">{error}</p>}

          <div className="modal-actions">
            <button type="button" className="modal-btn modal-btn--cancel" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" className="modal-btn modal-btn--create" disabled={loading}>
              {loading ? 'Creating…' : 'Create Project'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CreateProject
