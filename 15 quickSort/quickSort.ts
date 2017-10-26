/**
 * Sorts an array using quick sort
 */
export function quickSort(array: number[]): number[] {
	array = array.slice();
	partition(array, 0, array.length);
	return array;
}

/**
 * Partitions the (begin, end) index of the array
 */
function partition(array: number[], begin: number, end: number): void {
	const length = end - begin;

	/** Terminate the recursion */
	if (length <= 1) return;

	/** Randomly select a pivot and move it to the head of the array */
	let pivot = begin + Math.floor(Math.random() * length);
	[array[begin], array[pivot]] = [array[pivot], array[begin]];
	pivot = begin;

	/** Loop through all the elements, partitioning around the pivot */
	for (let i = begin + 1; i < end; i++) {
		if (array[i] < pivot) {
			pivot++;
			[array[i], array[pivot]] = [array[pivot], array[i]];
		}
	}
	[array[pivot], array[begin]] = [array[begin], array[pivot]];

	/** Partition all the elements less than the pivot */
	partition(array, begin, pivot - 1);

	/** Partition all the elements more than the pivot */
	partition(array, pivot + 1, end);
}
