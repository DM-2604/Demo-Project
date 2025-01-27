let my_promise = new Promise((success, reject) => {
    let x = 4;
    if (x % 2 == 0) {
        success("It's even number");
    } else {
        reject("False");
    }
});

my_promise
    .then((m) => console.log(m)) 
    .catch((e) => console.log(e));  
Promise.all([
    Promise.resolve("Task 1 completed"),
    Promise.resolve("Task 2 completed"),
    Promise.resolve("Task 3 failed")
])
    .then((results) => console.log(results))
    .catch((error) => console.error(error));
Promise.any([
    Promise.reject("Task 1 failed"),
    Promise.reject("Task 2 completed"),
    Promise.reject("Task 3 completed")
])
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
async function myFunction() {
  return "Hello";
}
console.log(myFunction())