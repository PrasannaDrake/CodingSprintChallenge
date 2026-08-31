#include <stdio.h>
#include <stdlib.h>

#define MAX_M 100005

void find_youngest_member(int n, int m, int gifts[][2]) {
    int *in_degree = (int *)calloc(n + 1, sizeof(int));
    int *out_degree = (int *)calloc(n + 1, sizeof(int));

    for (int i = 0; i < m; i++) {
        int giver = gifts[i][0];
        int receiver = gifts[i][1];
        out_degree[giver]++;
        in_degree[receiver]++;
    }

    int youngest = -1;
    for (int i = 1; i <= n; i++) {
        if (out_degree[i] == 0 && in_degree[i] == n - 1) {
            youngest = i;
            break;
        }
    }

    if (youngest != -1) {
        printf("\nThe youngest member is: %d\n", youngest);
    } else {
        printf("\nNo valid youngest member found: -1\n");
    }

    free(in_degree);
    free(out_degree);
}

static int gifts[MAX_M][2];

int main() {
    int n, m;

    // Prompt for n and m
    printf("Enter total members (n) and gift exchanges (m): ");
    fflush(stdout); // Forces the prompt to print immediately
    if (scanf("%d %d", &n, &m) != 2) return 0;

    // Prompt for exchanges
    printf("\nEnter %d gift exchanges (format: giver receiver):\n", m);
    for (int i = 0; i < m; i++) {
        printf("Exchange %d: ", i + 1);
        fflush(stdout); // Forces "Exchange X: " to print before scanf waits
        scanf("%d %d", &gifts[i][0], &gifts[i][1]);
    }

    find_youngest_member(n, m, gifts);

    return 0;
}