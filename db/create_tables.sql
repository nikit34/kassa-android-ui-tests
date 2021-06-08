CREATE TABLE metric_autotests.public.click_timeout (
    id_test integer,
    click real,
    date_time timestamp
);

CREATE TABLE metric_autotests.public.find_element_timeout (
    id_test integer,
    find_element real,
    date_time timestamp
);

CREATE TABLE metric_autotests.public.name_test (
    id_test integer,
    name_test text
);

CREATE INDEX idx_click_timeout ON metric_autotests.public.click_timeout (click);
CREATE INDEX idx_find_element_timeout ON metric_autotests.public.find_element_timeout (find_element);
