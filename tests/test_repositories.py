from dataclasses import asdict

import pytest

from tests.helpers import generate_admin_id


@pytest.mark.asyncio
async def test_admin_persistent_repo_save(
    mysql_manage, admin_persistent_repo, admin_dummy_set
):
    repo = admin_persistent_repo
    test_data = asdict(admin_dummy_set[0])

    await repo.save(test_data)


@pytest.mark.asyncio
async def test_admin_persistent_repo_patch(
    mysql_manage, admin_persistent_repo, save_admin_dummy_to_db
):
    repo = admin_persistent_repo

    await repo.patch(generate_admin_id(0), {"admin_type": "INTERVIEW"})

