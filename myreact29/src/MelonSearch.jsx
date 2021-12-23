import { Input } from 'antd';
import { useState } from 'react';

import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';

import { List, Avatar } from 'antd';
import { Menu, Dropdown } from 'antd';
import { DownOutlined } from '@ant-design/icons';

function MelonSearch() {
    const [query, setQuery] = useState("");
    const [songList, setSongList] = useState([]);
    
    const handleChange = (e) => {
      const { target: { value } } = e;
      console.group("handleChange");
      console.log(value);
      console.groupEnd();
      setQuery(value);
    };
    const handlePressEnter = () => {
      console.group("handlePressEnter");
      console.log(`검색어 ${query}로 검색합니다.`);
      console.groupEnd();

      const url = 'https://www.melon.com/search/keyword/index.json';

      Axios({
        url : url,
        adapter: jsonpAdapter,
        callbackParamName: 'jscallback',
        params: {
          query: query,
        },
      })
        .then((response) => {
          // ALBUMCONTENTS, ARTISTCONTENTS
          const { 
            data: { SONGCONTENTS: searchedSongList },
          } = response;

          console.group("멜론 검색결과");
          console.log(response);
          console.log(searchedSongList);
          console.groupEnd();

          setSongList(searchedSongList);
        })
        .catch((error) => {
          console.group("멜론 검색 에러");
          console.error(error);
          console.groupEnd();
        });
    };
    
    const menu = (
      <Menu>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="https://www.melon.com/index.htm">
            Artist ID :
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="https://www.melon.com/index.htm">
            SongName DP :
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="https://www.melon.com/index.htm">
            Song ID :
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="https://www.melon.com/index.htm">
            Album Name :
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="https://www.melon.com/index.htm">
            Album ID :
          </a>
        </Menu.Item>
      </Menu>
    );

    return (
      <div style={({width: 700, margin: '0 auto'})}>
        <h2>노래 검색</h2><br />
        검색어 : {query} <br />
        <Input style={({width: 300, margin: '0 auto'})}
          placeholder='검색어를 입력해주세요.'
          onChange={handleChange}
          onPressEnter={handlePressEnter}
        />
        <List style={({width: 650})}
          className="demo-loadmore-list"
          itemLayout="horizontal"
          dataSource={songList}
          renderItem={(item) => (
          <List.Item>
            <List.Item.Meta
              avatar={<Avatar src={item.ALBUMIMG} />}
              title={
                <a href="https://www.melon.com/index.htm">[{item.SONGNAME}] - Song ID : {item.SONGID}</a>
              }
              description={`ALBUM :: ${item.ALBUMNAME}`}
            />
        <div>
          <Dropdown overlay={menu}>
            <a className="ant-dropdown-link" onClick={e => e.preventDefault()}>
              {item.ARTISTNAME} <DownOutlined />
            </a>
          </Dropdown>
        </div>
          </List.Item>
        )}
      />
    </div>
  );
}

export default MelonSearch;