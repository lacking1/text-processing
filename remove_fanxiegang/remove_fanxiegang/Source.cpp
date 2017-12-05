#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
	string wavDataIndex = "wavnameList.txt";
	ifstream fileIndex(wavDataIndex.c_str());
	string wavSongName;
	static int totalWavSong = 0;//wav文件数
	//string SongName = "waveFile\\year2003\\person00002\\00041.wav";
	//在基线系统中的wavname，系统中有\\，写出来时是单斜杠

	ofstream wavSongNametemp("newNameList.txt", ofstream::app);
	while (fileIndex >> wavSongName)
	{
		totalWavSong++;
		//去掉三个斜杠，以便读取以此命名的txt
		wavSongName.erase(wavSongName.find("\\"), 1);
		wavSongName.erase(wavSongName.find("\\"), 1);
		wavSongName.erase(wavSongName.find("\\"), 1);
		
		wavSongNametemp << wavSongName << endl;
	}
	wavSongNametemp.close();
	cout << totalWavSong;
	system("Pause");
	return 0;
}


