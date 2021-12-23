// import Counter from "Counter";
// import MelonTop100 from "MelonTop100";

import MelonSearch from "MelonSearch";
import { PageHeader } from 'antd';


function App() {
  return (
    <div>
      <PageHeader
        className="site-page-header"
        title="MELON"
        subTitle="with React"
      />,
      <MelonSearch />
      {/* <MelonTop100 />
      <Counter />
      <Counter />
      <Counter /> */}
    </div>
  );
}

export default App;
