document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault(); 
    const data = {
        MedInc: document.getElementById('MedInc').value,
        HouseAge: document.getElementById('HouseAge').value,
        AveRooms: document.getElementById('AveRooms').value,
        AveBedrms: document.getElementById('AveBedrms').value,
        Population: document.getElementById('Population').value
    };
    const btn = document.querySelector('button');
    btn.innerText = "Predicting...";
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result-box').classList.remove('hidden');
        document.getElementById('price-output').innerText = "$ " + result.prediction.toLocaleString();
        btn.innerText = "Predict Price"; 
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Kuch error aayi hai. Backend check karo!");
        btn.innerText = "Predict Price";
    });
});