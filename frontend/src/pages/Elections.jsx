import "./Elections.css";

function Elections() {
  const elections = [
    {
      id: 1,
      title: "Student Union Election 2026",
      organization: "University Student Union",
      status: "Live",
      description:
        "Vote for the candidates who will represent students in the upcoming academic year.",
    },
    {
      id: 2,
      title: "SRC Executive Election 2026",
      organization: "Student Representative Council",
      status: "Upcoming",
      description:
        "Choose the next team that will lead and represent the student community.",
    },
    {
      id: 3,
      title: "Tech Club Executive Election",
      organization: "University Tech Club",
      status: "Live",
      description:
        "Participate in the election of the next Tech Club executive team.",
    },
  ];

  return (
    <main className="elections-page">
      <section className="elections-hero">
        <span className="elections-badge">VOTERA ELECTIONS</span>

        <h1>
          Find an <span>election.</span>
        </h1>

        <p>
          Browse available elections and make your voice count.
        </p>

        <div className="elections-search">
          <span>⌕</span>

          <input
            type="text"
            placeholder="Search elections..."
          />
        </div>
      </section>

      <section className="elections-list-section">
        <div className="elections-section-header">
          <div>
            <span>AVAILABLE ELECTIONS</span>
            <h2>Choose an election</h2>
          </div>

          <p>
            Select an election to view its positions and candidates.
          </p>
        </div>

        <div className="elections-grid">
          {elections.map((election) => (
            <article
              className="election-card"
              key={election.id}
            >
              <div className="election-card-top">
                <span
                  className={`election-status ${election.status.toLowerCase()}`}
                >
                  <span className="status-dot"></span>
                  {election.status}
                </span>
              </div>

              <div className="election-card-content">
                <span className="election-organization">
                  {election.organization}
                </span>

                <h3>{election.title}</h3>

                <p>{election.description}</p>
              </div>

              <button className="election-button">
                View Election
                <span>→</span>
              </button>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

export default Elections;