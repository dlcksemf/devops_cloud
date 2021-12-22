Array.prototype.sum = function () {
    return this.reduce((acc, element) => acc + element, 0);
};

const result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].sum();

console.log(result)