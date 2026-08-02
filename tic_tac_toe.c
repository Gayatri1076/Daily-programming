#include <stdio.h>

char board[3][3] = {
    {'1','2','3'},
    {'4','5','6'},
    {'7','8','9'}
};

void displayBoard() {
    printf("\n");
    for(int i=0;i<3;i++) {
        for(int j=0;j<3;j++) {
            printf(" %c ", board[i][j]);
            if(j<2) printf("|");
        }
        if(i<2) printf("\n-----------\n");
    }
    printf("\n");
}

int checkWin() {
    for(int i=0;i<3;i++) {
        if(board[i][0]==board[i][1] && board[i][1]==board[i][2])
            return 1;
        if(board[0][i]==board[1][i] && board[1][i]==board[2][i])
            return 1;
    }

    if(board[0][0]==board[1][1] && board[1][1]==board[2][2])
        return 1;

    if(board[0][2]==board[1][1] && board[1][1]==board[2][0])
        return 1;

    return 0;
}

void makeMove(int pos, char mark) {
    int row = (pos - 1) / 3;
    int col = (pos - 1) % 3;

    if(board[row][col] != 'X' && board[row][col] != 'O')
        board[row][col] = mark;
    else
        printf("Invalid Move!\n");
}

int main() {
    int move;
    char player = 'X';

    for(int turn=0; turn<9; turn++) {

        displayBoard();

        printf("Player %c, Enter Position (1-9): ", player);
        scanf("%d", &move);

        if(move < 1 || move > 9) {
            printf("Invalid Position!\n");
            turn--;
            continue;
        }

        int row = (move - 1) / 3;
        int col = (move - 1) % 3;

        if(board[row][col]=='X' || board[row][col]=='O') {
            printf("Already Occupied!\n");
            turn--;
            continue;
        }

        makeMove(move, player);

        if(checkWin()) {
            displayBoard();
            printf("\n🎉 Player %c Wins!\n", player);
            return 0;
        }

        player = (player == 'X') ? 'O' : 'X';
    }

    displayBoard();
    printf("\nGame Draw!\n");

    return 0;
}