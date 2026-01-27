
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void showtask(vector<string> &task){
    cout << "---TO DO LIST----" << endl;
    for(int i = 0 ; i < task.size(); i++){
        cout << i + 1 << ". " << task[i] << endl;
    }
}

int main () {
    vector<string> tasks;
    string task;
    char choice;


    do{
        cout << "1 - Add a task ---- 2 - View tasks --- 3 - exit \n";
        cout << "Enter your choice: ";
        cin >> choice ;

        switch(choice){
            case '1':
            cout << "Enter your task: ";
            cin.ignore();
            getline(cin,task);
            tasks.push_back(task);
            cout << "\n";
            break;

            case '2':
            showtask(tasks);
            break;
        }
    }while(choice != '3');

    return 0;

}