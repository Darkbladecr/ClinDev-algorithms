/**
 * Write a program that prints the integers from 1 to 100 (inclusive).
 * But:
 *  - for multiples of three, print Lub (instead of the number)
 *  - for multiples of five, print Dub (instead of the number)
 *  - for multiples of both three and five, print LubDub (instead of the number)
 */

for (let index = 1; index < 101; index++) {
	const isLub = index % 3 === 0;
	const isDub = index % 5 === 0;
	const result =
		isLub && isDub ? 'LubDub' : isLub ? 'Lub' : isDub ? 'Dub' : index;
	console.log(result);
}
