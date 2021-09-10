#!/usr/bin/node
/**
 * Displays a string!.
 * @returns {str} a string
 */
export function taskFirst () {

    const task = 'I prefer const when I can.';

    return task;

}

/**
 * Displays a string.
 * @returns {str} a string
 */
export function getLast () {

    return ' is okay';

}

/**
 * Displays a string.
 * @returns {str} a string
 */
export function taskNext () {

    let combination = 'But sometimes let';

    combination += getLast();

    return combination;

}
