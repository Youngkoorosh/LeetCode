func romanToInt(s string) int {
	romeAlpha := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	answer := 0

	for i := 0; i < len(s); i++ {
		current := romeAlpha[s[i]]

		if i+1 < len(s) && current < romeAlpha[s[i+1]] {
			answer -= current
		} else {
			answer += current
		}
	}

	return answer
}