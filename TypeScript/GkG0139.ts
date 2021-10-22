const transformCoffeeIntoCode = () => {
    fetch("https://api.github.com/repos/GkG0139/Coffee/readme")
        .then(response => response.json())
        .then(data => {
            alert(atob(data.content));
        })
        .catch(error => console.log(error));
}

const input = prompt('Type "coffee" ☕!');

if (input?.toLocaleLowerCase() === "coffee")
    transformCoffeeIntoCode();
