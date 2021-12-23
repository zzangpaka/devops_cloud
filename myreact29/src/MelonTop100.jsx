import { useState } from "react";
import { Button as BootstrapButton } from "react-bootstrap";
import { Button as AntdButton } from "antd";
import initialSongList from "./data/melon_data.json";
import "MelonTop100.css";

// 전역 변수 : 바뀌지 않는 데이터
//      - 초기값을 정의

function MelonTop100() {
    const [songList, setSongList] = useState([]);

    const handleClick = () => {
      setSongList(initialSongList);
    };

    return (
        <div>
            <h2>멜론 top 100</h2>
            <BootstrapButton variant="success" onClick={handleClick}>로딩</BootstrapButton>
            <AntdButton type="primary" onClick={handleClick}>로딩</AntdButton>
            <ul className="songList">
                {
                    songList.map(song => {
                        return <li key={song.song_no}>{song.rank} {song.title} {song.artist}</li>;
                    })
                }
            </ul>
        </div>
    );
}

export default MelonTop100;
