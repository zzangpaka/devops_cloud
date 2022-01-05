function Review({ review, onClick }) {
  return (
    <div
      className="bg-white my-1 p-1
      border-2 border-gray-500 
      hover:bg-gray-100 
      cursor-pointer"
      onClick={onClick}
    >
      {review.content.split('\n').map((line) => (
        <>
          {line}
          <br />
        </>
      ))}
      {review.rate}
    </div>
  );
}

export default Review;
