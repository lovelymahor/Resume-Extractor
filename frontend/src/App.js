import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!file) {
      alert("Please upload a resume first");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/analyze",
        formData
      );

      setResult(res.data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 AI Career Copilot</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        Analyze Resume
      </button>

      <hr />

      {result && (
        <div
          style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid #ddd",
            borderRadius: "10px",
            backgroundColor: "#f9f9f9"
          }}
        >
          <h2>📊 Resume Score: {result.score}/100</h2>

          {/* Progress Bar */}
          <div
            style={{
              height: "20px",
              width: "100%",
              backgroundColor: "#eee",
              borderRadius: "10px",
              overflow: "hidden",
              marginBottom: "15px"
            }}
          >
            <div
              style={{
                height: "100%",
                width: `${result.score}%`,
                backgroundColor:
                  result.score > 70 ? "green" : "orange"
              }}
            ></div>
          </div>

          <h3>📌 Suggestions:</h3>
          <ul>
            {result.feedback.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>💼 Career Suggestions:</h3>
          <ul>
            {result.career.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;