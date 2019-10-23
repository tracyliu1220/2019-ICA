#include <bits/stdc++.h>
using namespace std;

void print(int id) {
    cout << "print(p" << id << ")\n";
}

void genList(int dim) {
    cout << '[' << rand() % 1000;
    for (int i = 1; i < dim; i ++)
        cout << ',' << rand() % 1000;
    cout << ']';
}

void genPList(int size, int n) {
    cout << '[' << 'p' << rand() % n;
    for (int i = 1; i < size; i ++)
        cout << ',' << 'p' << rand() % n;
    cout << ']';
}

void genCertainPList(int id, int size, int n) {
    cout << '[' << 'p' << id;
    for (int i = 1; i < size; i ++)
        cout << ',' << 'p' << rand() % n;
    cout << ']';
}

void init(int id, int dim) {
    cout << "p" << id << "=Point(";
    int op = int(rand()) % 4;
    if (op == 0) {
        genList(dim);    
    } else if (op == 1) {
        cout << '(' << rand() % 1000;
        for (int i = 1; i < dim; i ++)
            cout << ',' << rand() % 1000;
        cout << ')';
    } else {
        cout << 'p' << rand() % id;
    }
    cout << ")\n";
    print(id);
}

void methods(int id, int dim, int ref) {
    cout << "p" << id << ".";
    int op = int(rand()) % 3;
    if (op == 0) {
        cout << "moveBy(";
        genList(dim);
        cout << ")\n";
    } else if (op == 1) {
        cout << "moveTo(";
        genList(dim);
        cout << ")\n";
    } else if (op == 2) {
        cout << "distanceTo(";
        cout << "p" << ref;
        cout << ")\n";
    }
    print(id);
}

void items(int id, int key) {
    int op = rand() % 2;
    if (op) { // get
        cout << "print(p" << id << "[" << key << "])\n";
    } else {
        cout << "p" << id << "[" << key << "]=" << rand() % 1000 << '\n';
        print(id);
    }
}


string ops[] = {"+", "-", ">", "==", " "};

void operators(int id1, int id2) {
    int op = rand() % 6;
    if (op <= 2) {
        cout << "print(p" << id1 << ops[op] << "p" << id2 << ")\n";
    } else if (op == 3) {
        cout << "print(p" << id1 << "==" << "p" << id2 << ")\n";
    } else if (op == 4) {
        float s = (rand() % 50) * 0.8;
        cout << "print(" << s << "*p" << id1 << ")\n";
    } else {
        int s = rand() % 50;
        cout << "print(" << s << "*p" << id1 << ")\n";
    }
}

void classMethod(int id, int size, int n) {
    int op = rand() % 2;
    if (op) {
        cout << "p" << id << "=Point.centroid(";
        genPList(size, n);
        cout << ")\n";
    } else {
        cout << "p" << id << "=p" << rand() % n << ".centroid(";
        genPList(size, n);
        cout << ")\n";
    }
    print(id);
}

void randomChoice(int id, int id2, int key, int dim, int n) {
    int op = rand() % 3;
    if (op == 0) {
        methods(id, dim, id2);
    } else if (op == 1) {
        operators(id, id2);
    } else if (op == 2) {
        cout << "p" << n+1 << "=Point.centroid(";
        genCertainPList(id, 10, n);
        cout << ")\n";
    }
}

int main() {
    int n = 10;
    int dim = 5;

    srand(time(NULL));

    // init
    for (int i = 0; i < n; i ++) {
        init(i, dim);
    }

    // methods
    int m = 10;
    for (int i = 0; i < m; i ++) {
        methods(rand() % n, dim, rand() % n);
    }

    // get/set items
    for (int i = 0; i < m; i ++) {
        items(rand() % n, rand() % dim);
    }

    // operators
    for (int i = 0; i < m; i ++) {
        operators(rand() % n, rand() %n);
    }

    // classmethod
    for (int i = 0; i < m; i ++) {
        classMethod(rand() % n, 10, n);
    }

    // exception
    cout << "p" << n << "=Point(";
    genList(dim + 3);
    cout << ")\n";
    for (int i = 0; i < m; i ++) {
        randomChoice(n, rand() % n, rand() % dim, dim, n);
    }
}
