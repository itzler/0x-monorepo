module TypeDoc.Factories
{
    /**
     * A factory that filters declarations that should be ignored and prevents
     * the creation of reflections for them.
     *
     * TypeDoc currently ignores all type aliases, object literals, object types and
     * implicit variables. Furthermore declaration files are ignored.
     */
    export class NullHandler extends BaseHandler
    {
        constructor(dispatcher:Dispatcher) {
            super(dispatcher);

            dispatcher.on(Dispatcher.EVENT_BEGIN_DOCUMENT, this.onEnterDocument, this, 1024);
            dispatcher.on(Dispatcher.EVENT_BEGIN_DECLARATION, this.onEnterDeclaration, this, 1024);
        }


        onEnterDocument(state:DocumentState) {
            if (state.document.isDeclareFile() && state.document.fileName.substr(-8) == 'lib.d.ts') {
                state.stopPropagation();
                state.preventDefault();
            }

            // Ignore declare files
            if (state.document.isDeclareFile()) {
                var settings = state.dispatcher.application.settings;
                if (state.document.fileName.substr(-8) != 'lib.d.ts' && settings.includeDeclarations) {
                    var childState = state.createChildState(state.document.topLevelDecl());
                    this.dispatcher.ensureReflection(childState);
                    this.dispatcher.processState(childState);
                }

                state.stopPropagation();
                state.preventDefault();
            }
        }


        onEnterDeclaration(state:DeclarationState) {
            // Ignore all type aliases, object literals and types
            if (state.kindOf([Models.Kind.ObjectLiteral, Models.Kind.ObjectType, Models.Kind.TypeAlias, Models.Kind.FunctionType, Models.Kind.FunctionExpression])) {
                state.stopPropagation();
                state.preventDefault();
            }

            // Ignore all implicit variables
            if (state.kindOf(Models.Kind.Variable) && state.hasFlag(Models.Flags.ImplicitVariable)) {
                state.stopPropagation();
                state.preventDefault();
            }
        }
    }


    Dispatcher.HANDLERS.push(NullHandler);
}