//SPDX-License-Identifier:MIT
pragma solidity ^0.8.3;

contract TodoList {
    struct Todo {
        string action;
        uint256 day;
        uint256 month;
        uint256 year;
    }
    Todo[] internal todoarr;

    constructor() payable {}

    function addtolist(
        string memory _action,
        uint256 _day,
        uint256 _month,
        uint256 _year
    ) external {
        todoarr.push(
            Todo({action: _action, day: _day, month: _month, year: _year})
        );
    }

    function getfromlist(uint256 _index)
        public
        view
        returns (
            string memory,
            uint256,
            uint256,
            uint256
        )
    {
        Todo memory todo = todoarr[_index];
        return (todo.action, todo.day, todo.month, todo.year);
    }

    function remfromtodo(uint256 index) external {
        todoarr[index] = todoarr[todoarr.length - 1];
        todoarr.pop();
    }

    function editwholeindex(
        uint256 index,
        string memory _action,
        uint256 _day,
        uint256 _month,
        uint256 _year
    ) external {
        Todo storage tod = todoarr[index];
        tod.action = _action;
        tod.day = _day;
        tod.month = _month;
        tod.year = _year;
    }

    function editaction(uint256 index, string memory _action) external {
        Todo storage todos = todoarr[index];
        todos.action = _action;
    }

    function editDay(uint256 index, uint256 _day) external {
        Todo storage todos = todoarr[index];
        todos.day = _day;
    }

    function editMonth(uint256 index, uint256 _month) external {
        Todo storage todos = todoarr[index];
        todos.month = _month;
    }

    function editYear(uint256 index, uint256 _year) external {
        Todo storage todos = todoarr[index];
        todos.year = _year;
    }

    function getlast()
        external
        view
        returns (
            string memory,
            uint256,
            uint256,
            uint256
        )
    {
        Todo storage aba = todoarr[todoarr.length - 1];
        return (aba.action, aba.day, aba.month, aba.year);
    }

    function getamnt() external view returns (uint256) {
        uint256 index = todoarr.length;
        return index;
    }

    function showaction(uint256 index) external view returns (string memory) {
        Todo storage todos = todoarr[index];
        return todos.action;
    }

    function showday(uint256 index) external view returns (uint256) {
        Todo storage todos = todoarr[index];
        return todos.day;
    }

    function showmonth(uint256 index) external view returns (uint256) {
        Todo storage todos = todoarr[index];
        return todos.month;
    }

    function showyear(uint256 index) external view returns (uint256) {
        Todo storage todos = todoarr[index];
        return todos.year;
    }

    function allTod() public view returns (Todo[] memory) {
        return todoarr;
    }
}
