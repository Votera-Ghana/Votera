import "./ElectionCard.css";

function ElectionCard({ election }) {
  const statusClass = election.status.toLowerCase();

  return (
    <article className="election-card">
      {/* Election Image */}
      <div className="election-card-image">
        <img
          src={election.image}
          alt={`${election.title} election`}
        />

        <span className={`election-status ${statusClass}`}>
          <span className="status-dot"></span>
          {election.status}
        </span>
      </div>

      {/* Election Information */}
      <div className="election-card-content">
        <span className="election-organization">
          {election.organization}
        </span>

        <h3>{election.title}</h3>

        <p>{election.description}</p>

        {/* Election Dates */}
        <div className="election-meta">
          <div>
            <span className="meta-label">Starts</span>
            <span className="meta-value">{election.startDate}</span>
          </div>

          <div>
            <span className="meta-label">Ends</span>
            <span className="meta-value">{election.endDate}</span>
          </div>
        </div>
      </div>

      {/* Action */}
      <div className="election-card-action">
        <button className="election-button">
          View Election
          <span>→</span>
        </button>
      </div>
    </article>
  );
}

export default ElectionCard;