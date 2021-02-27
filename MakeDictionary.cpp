#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) {
	ofstream outfile;
	outfile.open("data.txt",ios::app);
	char i = 000000;
	for(int i = 0;i<1000000;i++){
	outfile <<setw(6)<<setfill('0')<<i<<"\n";
	}
	outfile.close();
	cout<<"ok"<<endl;
}