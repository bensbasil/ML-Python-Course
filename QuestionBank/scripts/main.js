document.addEventListener('DOMContentLoaded', function() {
    const levels = [1, 2, 3];
    levels.forEach(level => {
      fetch(`../level-${level}/questions-level${level}.json`)
        .then(response => response.json())
        .then(data => {
          const container = document.getElementById(`level-${level}-questions`);
          data.forEach(question => {
            const questionElement = document.createElement('div');
            questionElement.classList.add('card', 'mt-3');
            questionElement.innerHTML = `
              <div class="card-body">
                <h5 class="card-title">${question.question}</h5>
                <p class="card-text">${question.answer}</p>
              </div>
            `;
            container.appendChild(questionElement);
          });
        });
    });
  });
  