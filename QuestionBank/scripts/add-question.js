document.getElementById('questionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const question = document.getElementById('question').value;
    const answer = document.getElementById('answer').value;
    const level = document.getElementById('level').value;
    
    const newQuestion = { question, answer };
  
    fetch(`../level-${level}/questions-level${level}.json`)
      .then(response => response.json())
      .then(data => {
        data.push(newQuestion);
        return fetch(`../level-${level}/questions-level${level}.json`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
      })
      .then(response => response.json())
      .then(() => {
        alert('Question added successfully!');
        window.location.href = 'index.html';
      });
  });
  