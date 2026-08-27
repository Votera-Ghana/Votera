import { Link } from "react-router-dom";

import "./CandidateCard.css";

function CandidateCard({ candidate, position, electionId }) {
  return (
    <article className="candidate-card">
      <div className="candidate-card-image">
        <img
          src={candidate.image}
          alt={candidate.name}
        />
      </div>

      <div className="candidate-card-content">
        <span className="candidate-position">
          {position}
        </span>

        <h4>{candidate.name}</h4>

        {candidate.bio && (
          <p>{candidate.bio}</p>
        )}

        <Link
          to={`/elections/${electionId}/candidate/${candidate.id}`}
          className="candidate-profile-button"
        >
          View Candidate
          <span> → </span>
        </Link>
      </div>
    </article>
  );
}

export default CandidateCard;