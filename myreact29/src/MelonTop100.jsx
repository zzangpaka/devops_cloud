import { useState } from "react";

// 전역 변수 : 바뀌지 않는 데이터
//      - 초기값을 정의
const initialSongList = [
    {
        "Unnamed: 0": 0,
        "song_no": 32872978,
        "title": "Dynamite",
        "album": "Dynamite (DayTime Version)",
        "artist": "방탄소년단",
        "rank": 1,
        "like": 354655
    },
    {
        "Unnamed: 0": 1,
        "song_no": 33077590,
        "title": "VVS (Feat. JUSTHIS) (Prod. GroovyRoom)",
        "album": "쇼미더머니 9 Episode 1",
        "artist": "미란이",
        "rank": 2,
        "like": 40716
    },
    {
        "Unnamed: 0": 2,
        "song_no": 32998018,
        "title": "힘든 건 사랑이 아니다",
        "album": "힘든 건 사랑이 아니다",
        "artist": "임창정",
        "rank": 3,
        "like": 74236
    },
];

function MelonTop100() {
    const [songList, setSongList] = useState([]);

    const handleClick = () => {
      setSongList(initialSongList);
    };

    return (
        <div>
            <h2>멜론 top 100</h2>
            <button onClick={handleClick}>로딩</button>
            <ul>
                {
                    songList.map(song => {
                        return <li>{song.title}</li>;
                    })
                }
                <li>제목1</li>
                <li>제목2</li>
                <li>제목3</li>
            </ul>
        </div>
    );
}

export default MelonTop100;
