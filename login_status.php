<?php
/**
 * Moodle login status checker.
 * Place this file in the root directory of your Moodle installation.
 * It will be requested by app.js to determine if the user is currently logged in.
 */

// Define AJAX_SCRIPT so Moodle knows this is a lightweight JSON response and doesn't load full UI HTML templates
define('AJAX_SCRIPT', true);

// Include Moodle configuration file
require_once(__DIR__ . '/config.php');

// Enable CORS if the landing page is hosted on a different subdomain (e.g. www.alshamcenter.de accessing moodle.alshamcenter.de)
// Uncomment the line below and adjust the origin if needed:
// header('Access-Control-Allow-Origin: https://alshamcenter.de');
// header('Access-Control-Allow-Credentials: true');

header('Content-Type: application/json; charset=utf-8');

// Check if user is logged in and not a guest user
$isLoggedIn = isloggedin() && !isguestuser();

$response = [
    'loggedin' => $isLoggedIn,
];

// If logged in, you can optionally expose additional information (e.g., username, name)
if ($isLoggedIn) {
    global $USER;
    $response['username'] = $USER->username;
    $response['fullname'] = fullname($USER);
}

echo json_encode($response);
