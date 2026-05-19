
import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setTeams(results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Teams</h2>
        {teams.length === 0 ? (
          <div className="alert alert-info">No teams found.</div>
        ) : (
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-light">
                <tr>
                  {Object.keys(teams[0]).map((key) => (
                    <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {teams.map((team, idx) => (
                  <tr key={team.id || idx}>
                    {Object.values(team).map((value, i) => (
                      <td key={i}>{typeof value === 'object' ? JSON.stringify(value) : value}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default Teams;
