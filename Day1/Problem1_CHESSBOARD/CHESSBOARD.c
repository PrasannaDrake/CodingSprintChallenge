#include <stdio.h>
#include <string.h>
#include <ctype.h>

const char* determine_color(const char* s) {
    // Rule 1: Input String Length must be exactly 2 characters
    if (strlen(s) != 2) {
        return "Incorrect input";
    }

    // Convert first character to lowercase so 'B' becomes 'b'
    char col_char = tolower(s[0]);
    char row_char = s[1];

    // Rule 2: First char must be a column from 'a' to 'h'
    if (col_char < 'a' || col_char > 'h') {
        return "Incorrect input";
    }

    // Rule 3: Second char must be a row digit from '1' to '8'
    if (row_char < '1' || row_char > '8') {
        return "Incorrect input";
    }

    // Map column 'a'-'h' to integer 1-8
    int col = col_char - 'a' + 1;
    // Map row character '1'-'8' to integer 1-8
    int row = row_char - '0';

    // Even sum = Black, Odd sum = White
    if ((col + row) % 2 == 0) {
        return "Black";
    } else {
        return "White";
    }
}

int main() {
    char s[256];

    // Prompt user for input
    printf("Enter Chess Square (e.g. a2): ");

    if (scanf("%255s", s) == 1) {
        const char* result = determine_color(s);
        printf("%s\n", result);
    }

    return 0;
}