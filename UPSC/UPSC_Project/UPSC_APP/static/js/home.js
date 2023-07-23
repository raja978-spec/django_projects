document.addEventListener("DOMContentLoaded", function () {
  const rowsPerPage = 5;
  const table = document.getElementById("data-table");
  const filterInput = document.getElementById("filter");
  const prevPageBtn = document.getElementById("prevPage");
  const nextPageBtn = document.getElementById("nextPage");
  const currentPageSpan = document.getElementById("currentPage");
  const totalPagesSpan = document.getElementById("totalPages");

  let currentPage = 1;

  function updatePaging() {
    const rows = table.getElementsByTagName("tr");
    const totalRows = rows.length - 1; // Subtract 1 to exclude the header row
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    // Ensure current page is within valid range
    currentPage = Math.max(1, Math.min(currentPage, totalPages));

    // Hide all rows first
    for (let i = 1; i < rows.length; i++) {
      rows[i].style.display = "none";
    }

    // Show only the rows for the current page
    const startIndex = (currentPage - 1) * rowsPerPage + 1;
    const endIndex = Math.min(startIndex + rowsPerPage, rows.length);
    for (let i = startIndex; i < endIndex; i++) {
      rows[i].style.display = "table-row";
    }

    // Update pagination text
    currentPageSpan.textContent = currentPage;
    totalPagesSpan.textContent = totalPages;
  }

  function handleFilter() {
    const filterValue = filterInput.value.toLowerCase();
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.getElementsByTagName("td");
      let showRow = false;

      for (let j = 0; j < cells.length; j++) {
        const cellValue = cells[j].textContent.toLowerCase();
        if (cellValue.includes(filterValue)) {
          showRow = true;
          break;
        }
      }

      row.style.display = showRow ? "table-row" : "none";
    }
    updatePaging();
  }

  function prevPage() {
    currentPage--;
    updatePaging();
  }

  function nextPage() {
    currentPage++;
    updatePaging();
  }

  filterInput.addEventListener("keyup", handleFilter);
  prevPageBtn.addEventListener("click", prevPage);
  nextPageBtn.addEventListener("click", nextPage);

  updatePaging();
});
