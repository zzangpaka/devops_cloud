function TopNav({ changePage }) {
  return (
    <div>
      <span>
        <button onClick={() => changePage("Lotto")}>Lotto</button>
      </span>
      <span>
        <button onClick={() => changePage("Member1")}>Profile Card</button>
      </span>
    </div>
  );
}

export default TopNav;
