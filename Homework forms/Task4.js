window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const row = document.querySelector('.row');
    let currentCol = 3;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const textR = document.querySelector('input[name="textR"]').value;
        const textG = document.querySelector('input[name="textG"]').value;
        const textB = document.querySelector('input[name="textB"]').value;

        const newContainer = document.createElement('div');
        newContainer.classList.add('container');

        const newColorBox = document.createElement('div');
        newColorBox.classList.add('colorbox');
        newColorBox.style.backgroundColor = `rgb(${textR}, ${textG}, ${textB})`;

        const newText = document.createElement('div');
        newText.classList.add('text');
        newText.textContent = `RGB: ${textR}, ${textG}, ${textB}`;

        newContainer.appendChild(newColorBox);
        newContainer.appendChild(newText);

        const currentColElement = document.querySelector(`.col:nth-child(${currentCol})`);


        if (!currentColElement) {
            const newCol = document.createElement('div');
            newCol.classList.add('col');
            newCol.appendChild(newContainer);
            row.appendChild(newCol);
        } else {
            currentColElement.appendChild(newContainer);
        }


        currentCol = currentCol % 3 + 1;

        form.reset();
    });
});
