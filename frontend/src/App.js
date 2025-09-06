import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [articles, setArticles] = useState([]);
  const [nextPageUrl, setNextPageUrl] = useState(null);
  const [previousPageUrl, setPreviousPageUrl] = useState(null);

  const fetchArticles = (url) => {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setArticles(data.results);
        setNextPageUrl(data.next);
        setPreviousPageUrl(data.previous);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  };

  useEffect(() => {
    // Fetch the first page when the component mounts
    fetchArticles('http://127.0.0.1:8000/news/articles/');
  }, []);

  const handleNext = () => {
    if (nextPageUrl) {
      fetchArticles(nextPageUrl);
    }
  };

  const handlePrevious = () => {
    if (previousPageUrl) {
      fetchArticles(previousPageUrl);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 style={{color: 'white', fontSize: 24}}>
          Top Articles:
        </h1>
      </header>
      <div className="articles" id="articles" style={{ maxWidth: "600px", margin: "0 auto", padding: "20px", textAlign: "left", marginTop: "20px" }}>
        {articles.map((article, index) => (
          <div key={index} style={{marginBottom: 15, textAlign: 'left'}}>
            <div className="info" style={{display: 'flex', marginBlock: 10}}>
              <img src={article.image_url} style={{maxWidth: '35%', height: 'auto', marginTop: 5, marginRight: 10, marginLeft: 10, marginBottom: 10}} />
              <div>
                <a href={article.url} target="_blank" rel="noopener noreferrer" style={{color: '#61dafb', fontSize: 18}}>
                  {article.title}
                </a>
                <p style={{margin: 0, fontSize: 14}}>{article.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div style={{ marginTop: '20px' }}>
        {previousPageUrl && (
          <button variant="contained" color="primary" onClick={handlePrevious}>Previous</button>
        )}
        {nextPageUrl && (
          <button variant="contained" color="primary" onClick={handleNext} style={{ marginLeft: '10px' }}>Next</button>
        )}
      </div>
    </div>
  );
}

export default App;
