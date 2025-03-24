
import { MantineProvider, SimpleGrid, Text } from '@mantine/core';
import { createRoot } from 'react-dom/client';

/**
 * Render a custom dashboard item with the provided context
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function AusleihfunktionDashboardItem({
    context
}: {
    context: any;
}) {

    // Render a simple grid of data
    return (
        <SimpleGrid cols={2} spacing="md">
            <Text>Hello world</Text>
            <Text>
                Username: {context.user?.username?.()}
            </Text>
        </SimpleGrid>
    );
}


/**
 * Render the AusleihfunktionDashboardItem component.
 * 
 * @param target - The target HTML element to render the panel into
 * @param context - The context object to pass to the panel
 */
export function renderAusleihfunktionDashboardItem(target: HTMLElement, context: any) {
    createRoot(target).render(
        <MantineProvider>
            <AusleihfunktionDashboardItem context={context} />
        </MantineProvider>
    );
}
