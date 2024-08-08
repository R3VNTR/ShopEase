document.addEventListener('DOMContentLoaded', () => {
    function handleTabClick(activeTabId, activeContentId) {
        const tabs = ['active-tab', 'deleted-tab', 'myorder-tab', 'salesorders-tab'];
        const contents = ['active-content', 'deleted-content', 'myorder-content', 'salesorder-content'];

        // Show the active content and hide all other contents
        document.getElementById(activeContentId).classList.remove('hidden');
        contents.forEach(contentId => {
            if (contentId !== activeContentId) {
                document.getElementById(contentId).classList.add('hidden');
            }
        });

        // Update tab styles
        tabs.forEach(tabId => {
            const tab = document.getElementById(tabId);
            if (tabId === activeTabId) {
                tab.classList.add('bg-blue-100', 'text-blue-600');
                tab.classList.remove('bg-gray-100', 'text-gray-600');
            } else {
                tab.classList.add('bg-gray-100', 'text-gray-600');
                tab.classList.remove('bg-blue-100', 'text-blue-600');
            }
        });
    }

    document.getElementById('active-tab').addEventListener('click', () => {
        handleTabClick('active-tab', 'active-content');
    });

    document.getElementById('deleted-tab').addEventListener('click', () => {
        handleTabClick('deleted-tab', 'deleted-content');
    });

    document.getElementById('myorder-tab').addEventListener('click', () => {
        handleTabClick('myorder-tab', 'myorder-content');
    });

    document.getElementById('salesorders-tab').addEventListener('click', () => {
        handleTabClick('salesorders-tab', 'salesorder-content');
    });
});
