#include <iostream>
#include <fstream>
#include <chrono>
#include <map>
#include <string.h>
using namespace std;


map<string, map<int,int>> data;
int twNum;
int wdNum;
int kynum;
int getTwee();
int findKey(int* rtn);
int main(int argc, char *argv[]){

	int input = 1;
	while(input){
		cin >> input;
		if (input == 1){
				int rtn = getTwee();
			if (rtn != 0){
				cout << "fail to get twitter feeds." << endl;
			}
		}
		if (input == 2){
				int sorted[10];
				int rtn = findKey(sorted);
			if (rtn != 0){
				cout << "fail to get twitter feeds." << endl;
			}
			else{
				for(int i = 0; i < 10; i++){
					cout<<sorted[i]<<" ";
				}
				cout << endl;
			}
		}
	
	}
	

	

	cout<< data["sentence"][0]<<endl;
	cout<< data["sentence"][1];


	return 0;
}



int getTwee(){
	data.clear();
	ifstream infile;
	infile.open("twi.txt");
	if(!infile){
		cout << "Error opening twitter file " <<endl;
		return -1;
	} 

	string temp;
	infile >> twNum;
	string raw[twNum];
	for(int i = 0; i < twNum; i++){
		infile >> wdNum;
		raw[i] = "";
		for(int j = 0; j < wdNum; j++){
			infile >> temp;
			if(data.find(temp) == data.end()){
				map<int,int> inner;
				inner[i] = 1;
				data[temp] = inner;
			}
			else{
				if(data[temp].find(i) == data[temp].end()){
					data[temp][i] = 1;
				}
				else{
					data[temp][i] = data[temp][i] + 1;
				}
			}

		}
	}
	return 0;

}

int findKey(int* rtn){
	map <int,int> count;
	
	ifstream infile;
	infile.open("key.txt");
	if(!infile){
		cout << "Error opening key file " <<endl;
		return -1;
	}
	infile >> kynum;
	
	string key;
	for(int i = 0; i < kynum; i++){
		infile >> key;
		if (data.find(key) != data.end()){
			for(map<int,int> ::const_iterator it = data[key].begin();it != data[key].end(); ++it)
			{
				if(count.find(it->first) == count.end()){
					count[it->first] = it->second;
				}
				else{
					count[it->first] = count[it->first] + it->second;
				}
			}
		}
	}
	pair <int,int> sorted[11];
	for(int i = 0; i < 11; i++){
		sorted[i].first = -1;
		sorted[i].second = 0;
	}
	for(map<int,int> ::const_iterator it = count.begin();it != count.end(); ++it){
		int i;
		for(i = 9; i >= 0; i--){
			if(it->second <= sorted[i].second){
				break;
			}
		}
		
		for(int j = 9; j > i; j--){
			sorted[j+1].first = sorted[j].first;
			sorted[j+1].second = sorted[j].second;
		}
		sorted[i+1].first = it->first;
		sorted[i+1].second = it->second;
	}
	for(int i = 0; i < 10; i++){
		rtn[i] = sorted[i].first;
	}
	return 0;
}