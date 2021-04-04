/**
 * @param {string} coordinates
 * @return {boolean}
 */
var squareIsWhite = function(coordinates) {
    let char = coordinates[0], num = coordinates[1];
    if (char == 'a' || char == 'c' || char == 'e' || char == 'g') {
        return num % 2 == 0 ? true : false;
    }
    if (char == 'b' || char == 'd' || char == 'f' || char == 'h') {
        return num % 2 == 0 ? false : true;
    }
};