function ReviewForm({ fieldValues, handleChange, handleSubmit }) {
  return (
    <div>
      <div className="rounded border-2 border-pink-500 p-3 my-3">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            별점
          </label>
          <select
            onChange={handleChange}
            name="rate"
            value={fieldValues.rate}
            className="block appearance-none w-full bg-white border border-gray-300 
        text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none 
        focus:bg-white focus:border-gray-500"
          >
            <option>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            리뷰
          </label>
          <textarea
            className="shadow appearance-none border border-gray-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            name="content"
            onChange={handleChange}
            value={fieldValues.content}
          ></textarea>
        </div>
        <div className="mb-4">
          <button
            className="shadow border bg-pink-100 hover:bg-pink-300 border-pink-500 
          rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight"
            onClick={handleSubmit}
          >
            저장하기
          </button>
        </div>
      </div>
    </div>
  );
}

export default ReviewForm;
